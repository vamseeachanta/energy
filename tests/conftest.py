# conftest.py - Pytest configuration and shared fixtures for energy project

import pytest
import os
import tempfile
from pathlib import Path
from typing import Generator, Any
from unittest.mock import Mock, patch

# Set testing environment
os.environ['TESTING'] = 'true'
os.environ['DEBUG'] = 'false'


# Basic fixtures
@pytest.fixture(scope="session")
def project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture(scope="function")
def mock_logger():
    """Mock logger for testing."""
    return Mock()


@pytest.fixture(scope="function")
def sample_energy_data() -> dict[str, Any]:
    """Sample energy data for testing."""
    return {
        "id": 1,
        "name": "Test Energy System",
        "description": "A test energy system for testing purposes",
        "active": True,
        "capacity": 1000.0,
        "efficiency": 0.85,
        "metadata": {
            "created_at": "2025-01-01T00:00:00Z",
            "tags": ["test", "energy", "sample"],
            "location": {"lat": 40.7128, "lon": -74.0060}
        }
    }


@pytest.fixture(scope="function")
def sample_energy_metrics() -> dict[str, Any]:
    """Sample energy metrics for testing."""
    return {
        "timestamp": "2025-01-01T12:00:00Z",
        "power_output": 850.0,
        "efficiency": 0.85,
        "temperature": 25.5,
        "pressure": 1013.25,
        "wind_speed": 12.5,
        "solar_irradiance": 800.0
    }


# File system fixtures
@pytest.fixture(scope="function")
def temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create a temporary file for testing."""
    test_file = temp_dir / "test_file.txt"
    test_file.write_text("Test content")
    yield test_file


@pytest.fixture(scope="function")
def empty_temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create an empty temporary file for testing."""
    test_file = temp_dir / "empty_file.txt"
    test_file.touch()
    yield test_file


@pytest.fixture(scope="function")
def sample_csv_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create a sample CSV file for testing."""
    csv_file = temp_dir / "sample_data.csv"
    csv_content = """timestamp,power,efficiency
2025-01-01T00:00:00Z,850.0,0.85
2025-01-01T01:00:00Z,900.0,0.88
2025-01-01T02:00:00Z,750.0,0.82
"""
    csv_file.write_text(csv_content)
    yield csv_file


# Mock fixtures
@pytest.fixture(scope="function")
def mock_requests():
    """Mock requests library for HTTP testing."""
    with patch('requests.Session') as mock_session:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success", "data": []}
        mock_response.text = '{"status": "success", "data": []}'
        mock_session.return_value.get.return_value = mock_response
        mock_session.return_value.post.return_value = mock_response
        yield mock_session


@pytest.fixture(scope="function")
def mock_database():
    """Mock database connection for testing."""
    with patch('your_module.database') as mock_db:
        # Configure mock database behavior
        mock_db.connect.return_value = Mock()
        mock_db.execute.return_value = []
        mock_db.fetch_one.return_value = None
        mock_db.fetch_all.return_value = []
        yield mock_db


# Environment fixtures
@pytest.fixture(scope="function")
def test_env_vars():
    """Set test environment variables."""
    test_vars = {
        'TEST_MODE': 'true',
        'DEBUG': 'false',
        'DATABASE_URL': 'sqlite:///:memory:',
        'API_KEY': 'test-api-key',
        'ENERGY_API_URL': 'http://localhost:8000/api',
        'CACHE_TTL': '300'
    }

    # Store original values
    original_values = {}
    for key, value in test_vars.items():
        original_values[key] = os.environ.get(key)
        os.environ[key] = value

    yield test_vars

    # Restore original values
    for key, original_value in original_values.items():
        if original_value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = original_value


# Fixtures for specific testing scenarios
@pytest.fixture(scope="function")
def mock_time():
    """Mock time functions for consistent testing."""
    import time
    import datetime

    fixed_time = datetime.datetime(2025, 1, 1, 12, 0, 0)
    fixed_timestamp = fixed_time.timestamp()

    with patch('time.time', return_value=fixed_timestamp), \
         patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = fixed_time
        mock_datetime.utcnow.return_value = fixed_time
        yield fixed_time


@pytest.fixture(scope="function")
def captured_logs(caplog):
    """Capture log messages for testing."""
    import logging
    caplog.set_level(logging.DEBUG)
    yield caplog


# Custom markers
def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line("markers", "unit: mark test as a unit test")
    config.addinivalue_line("markers", "integration: mark test as an integration test")
    config.addinivalue_line("markers", "e2e: mark test as an end-to-end test")
    config.addinivalue_line("markers", "slow: mark test as slow running")
    config.addinivalue_line("markers", "api: mark test as an API test")
    config.addinivalue_line("markers", "database: mark test as requiring database")
    config.addinivalue_line("markers", "external: mark test as requiring external services")
    config.addinivalue_line("markers", "energy: mark test as energy-specific")


# Pytest hooks
def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "e2e" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)
            item.add_marker(pytest.mark.slow)

        # Add energy marker to all tests
        item.add_marker(pytest.mark.energy)