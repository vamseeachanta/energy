# Smoke tests for energy project
"""
Basic smoke tests to verify the project setup and essential functionality.

These tests ensure:
1. Python environment is correct
2. Project structure is valid
3. Essential imports work
4. Pytest configuration is working
5. Fixtures are available
6. Coverage configuration is working
"""

import sys
import os
import pytest
from pathlib import Path


class TestEnvironment:
    """Test environment and Python setup."""

    def test_python_version(self):
        """Test that Python version meets requirements."""
        # According to pyproject.toml, requires Python >=3.8
        major, minor = sys.version_info[:2]
        assert major == 3, f"Expected Python 3.x, got {major}.{minor}"
        assert minor >= 8, f"Expected Python 3.8+, got {major}.{minor}"

    def test_testing_environment_set(self):
        """Test that testing environment variables are set."""
        assert os.environ.get('TESTING') == 'true'
        # This should be set by conftest.py


class TestProjectStructure:
    """Test project structure and organization."""

    def test_project_root_exists(self, project_root):
        """Test that project root directory exists and is accessible."""
        assert project_root.exists()
        assert project_root.is_dir()

    def test_pyproject_toml_exists(self, project_root):
        """Test that pyproject.toml exists and is readable."""
        pyproject_file = project_root / "pyproject.toml"
        assert pyproject_file.exists()
        assert pyproject_file.is_file()

        # Try to read the file
        content = pyproject_file.read_text()
        assert "[project]" in content
        assert "name = \"energy\"" in content

    def test_tests_directory_structure(self, project_root):
        """Test that tests directory has proper structure."""
        tests_dir = project_root / "tests"
        assert tests_dir.exists()
        assert tests_dir.is_dir()

        # Check for __init__.py
        assert (tests_dir / "__init__.py").exists()

        # Check for subdirectories
        assert (tests_dir / "unit").exists()
        assert (tests_dir / "integration").exists()

        # Check for conftest.py
        assert (tests_dir / "conftest.py").exists()


class TestImports:
    """Test that essential imports work correctly."""

    def test_standard_library_imports(self):
        """Test that standard library imports work."""
        import os
        import sys
        import pathlib
        import unittest.mock
        import tempfile
        import typing

        # Basic smoke test - just ensure imports don't fail
        assert os is not None
        assert sys is not None
        assert pathlib is not None

    def test_testing_library_imports(self):
        """Test that testing libraries are available."""
        import pytest
        import unittest.mock

        # Test pytest is available and working
        assert pytest.__version__ is not None

        # Test that Mock is available
        from unittest.mock import Mock, patch
        mock_obj = Mock()
        assert mock_obj is not None

    def test_project_imports_basic(self):
        """Test that basic project imports work (if any exist)."""
        # This test will pass even if no project modules exist yet
        import sys

        # Check if src directory is in path (added by tests/__init__.py)
        project_root = Path(__file__).parent.parent
        src_dir = str(project_root / "src")

        # If src directory exists, it should be in sys.path
        if (project_root / "src").exists():
            assert src_dir in sys.path or any(src_dir in p for p in sys.path)


class TestPytestConfiguration:
    """Test that pytest configuration is working."""

    def test_pytest_markers_configured(self):
        """Test that custom pytest markers are configured."""
        # Test that markers are available (they should be configured in conftest.py)
        import pytest

        # These should not raise warnings when used
        pytest.mark.unit
        pytest.mark.integration
        pytest.mark.energy
        pytest.mark.slow

    def test_test_discovery_patterns(self):
        """Test that pytest can discover this test file."""
        # If pytest is running this test, discovery is working
        assert True

    def test_coverage_importable(self):
        """Test that coverage tools are available."""
        try:
            import coverage
            assert coverage is not None
        except ImportError:
            pytest.skip("Coverage not installed - this is okay for basic setup")


class TestFixtures:
    """Test that fixtures from conftest.py are working."""

    def test_project_root_fixture(self, project_root):
        """Test that project_root fixture works."""
        assert isinstance(project_root, Path)
        assert project_root.exists()
        assert project_root.name == "energy"

    def test_temp_dir_fixture(self, temp_dir):
        """Test that temp_dir fixture works."""
        assert isinstance(temp_dir, Path)
        assert temp_dir.exists()
        assert temp_dir.is_dir()

        # Test we can create files in it
        test_file = temp_dir / "test.txt"
        test_file.write_text("test")
        assert test_file.exists()

    def test_sample_energy_data_fixture(self, sample_energy_data):
        """Test that sample_energy_data fixture works."""
        assert isinstance(sample_energy_data, dict)
        assert "id" in sample_energy_data
        assert "name" in sample_energy_data
        assert "capacity" in sample_energy_data
        assert sample_energy_data["name"] == "Test Energy System"

    def test_mock_logger_fixture(self, mock_logger):
        """Test that mock_logger fixture works."""
        from unittest.mock import Mock
        assert isinstance(mock_logger, Mock)

        # Test that we can call methods on it
        mock_logger.info("test message")
        mock_logger.info.assert_called_once_with("test message")


class TestCoverageConfiguration:
    """Test that coverage configuration is working."""

    def test_coverage_config_in_pyproject(self, project_root):
        """Test that coverage configuration exists in pyproject.toml."""
        pyproject_file = project_root / "pyproject.toml"
        content = pyproject_file.read_text()

        # Check for coverage configuration sections
        assert "[tool.coverage.run]" in content
        assert "[tool.coverage.report]" in content

    def test_coverage_can_run(self):
        """Test that coverage can be imported and basic functionality works."""
        try:
            import coverage

            # Test basic coverage functionality
            cov = coverage.Coverage()
            assert cov is not None

        except ImportError:
            pytest.skip("Coverage not installed - may be okay for basic setup")

    def test_this_test_runs_with_coverage(self):
        """This test should show up in coverage reports."""
        # Simple test that exercises code that should be covered
        result = self._helper_method()
        assert result == "coverage_test"

    def _helper_method(self):
        """Helper method to test coverage detection."""
        return "coverage_test"


# Mark all tests in this file
pytestmark = pytest.mark.unit