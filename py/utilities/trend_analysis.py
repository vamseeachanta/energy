import pandas as pd
import plotly_express as px

class TrendAnalysis:

  def __init__(self):
    pass

  def find_dff_in_2_Dicts(self, cfg_ta):
    print("perform trend analysis")
    df = cfg_ta['df']
    print(df.columns)


if __name__ == '__main__':
  trend_analysis = TrendAnalysis()
  csv_filename = 'D:\\GitHub\\client_projects\\energy_firm_sd_support\\xom\\000 ENIGMA\\cod\\2022-04-15_incidents.csv'
  df = pd.read_csv(csv_filename)

  replace_dict = {
      '0 - No Hurt': 0,
      '1 - Minor Hurt': 1,
      '2 - Moderate Hurt': 2,
      '4 - Fatality': 4,
      '3 - Severe Hurt': 3,
      '5 - Multiple Fatalities': 5
  }
  df['actual_hurt_level_value'] = df['actual_hurt_level']
  df = df.replace({'actual_hurt_level_value': replace_dict})
  df['potential_hurt_level_value'] = df['potential_hurt_level']
  df = df.replace({'potential_hurt_level_value': replace_dict})

  cfg_ta = {'df': df, 'column': 'actual_hurt_level_value'}
  trend_analysis.find_dff_in_2_Dicts(cfg_ta)

  aggregation_columns = ['incident_date']
  agg_df_columns = aggregation_columns + ['count']
  sub_title = '<br><sup> Conclusions: TBA</sup>'
  x = aggregation_columns[0]

  work_activity_df = df.groupby(aggregation_columns, as_index=False).agg({
      'actual_hurt_level_value': ['sum'],
      'potential_hurt_level_value': ['sum']
  })
  px_work_activity_df = pd.DataFrame(columns=agg_df_columns)
  px_work_activity_df[agg_df_columns[0]] = work_activity_df[agg_df_columns[0]]
  px_work_activity_df.sort_values(by=agg_df_columns[0], inplace=True)
  px_work_activity_df['total_actual_hurt_index'] = work_activity_df[
      'actual_hurt_level_value']['sum']
  px_work_activity_df['total_potential_hurt_index'] = work_activity_df[
      'potential_hurt_level_value']['sum']

#   fig = px.line(px_work_activity_df,
#                 x=agg_df_columns[0],
#                 y=['total_actual_hurt_index', 'total_potential_hurt_index'],
#                 title=color + sub_title,
#                 height=800)
#   fig.update_layout(bargap=0.1)
#   fig.show()
