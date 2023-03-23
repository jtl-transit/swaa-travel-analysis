"""
Helper functions for processing SWAA data

"""

# Import useful libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from operator import ge, le

# Set global parameters for plt
figsize = [5,3]
plt.style.use('plot_style.txt')
plt.rcParams['figure.figsize'] = figsize

def filter_df(dataset, scale_col):
    # Personal Variables
    column_filter = []
    column_filter.append('date')                         # Survey wave
    column_filter.append('age_quant')                     # Continuous age
    column_filter.append('agebin')                       # Categorical age
    column_filter.append('educ_years')                   # Continuous education
    column_filter.append('education')                    # Categorical education
    column_filter.append('income')                       # Continuous income
    column_filter.append('income_cat')                   # Categorical income
    column_filter.append('gender')                       # Categorical gender
    column_filter.append('party_affiliation_s')          # Categorical party affiliation
    column_filter.append('disability_qual')              # Disability category
    
    # Attitudes
    column_filter.append('infectionfear_taxi')           # Fear of infection on mode
    column_filter.append('infectionfear_bus')            # Fear of infection on mode
    column_filter.append('infectionfear_subway')         # Fear of infection on mode
    column_filter.append('infectionfear_train')          # Fear of infection on mode
    column_filter.append('infectionfear_bikewalk')       # Fear of infection on mode
    column_filter.append('infectionfear_car')            # Fear of infection on mode
    column_filter.append('wfh_less_stress')              # Less stressed WFH
    column_filter.append('wfh_feel_quant_actual')              # Less stressed WFH
    column_filter.append('wfh_expect')              # Less stressed WFH
    column_filter.append('wfh_expect_quant')              # Less stressed WFH
    column_filter.append('wfh_Dperception')              # Less stressed WFH
    column_filter.append('wfh_able_quant')               # How possible is WFH?
    column_filter.append('wfh_eff_COVID_quant')          # Efficiency from WFH
    column_filter.append('wfh_eff_noCOVID_quant')          # Efficiency from WFH

    column_filter.append('wfh_top3benefits_commute')     # Top 3 benefits of WFH includes no commute
    column_filter.append('wfh_top3benefits_quiet')       # Top 3 benefits of WFH includes more quiet time
    column_filter.append('wfh_top3benefits_flex')        # Top 3 benefits of WFH includes more flexibility
    column_filter.append('wbp_top3benefits_equip')       # Top 3 benefits of Office includes better equipment
    column_filter.append('wbp_top3benefits_social')      # Top 3 benefits of Office includes socializing
    column_filter.append('wbp_top3benefits_bound')       # Top 3 benefits of Office includes work/life boundaries
    column_filter.append('wbp_top3benefits_quiet')       # Top 3 benefits of Office includes more quiet time
    column_filter.append('life_rank_work')               # Work = #1 life priority
    column_filter.append('life_rank_family')             # Work = #1 life priority
    column_filter.append('life_rank_leisure')            # Work = #1 life priority
    column_filter.append('life_rank_politics')           # Work = #1 life priority
    column_filter.append('life_rank_friends')            # Work = #1 life priority
    column_filter.append('life_rank_religion')           # Work = #1 life priority
    column_filter.append('work_firm_succeed')            # Willing to work harder to help firm succceed
    column_filter.append('factors_wfhsched_cow')         # Coordinating with coworkers is important
    column_filter.append('factors_wfhsched_traffic')     # Coordinating with traffic is important
    column_filter.append('videocall_small_qual')         # Effectiveness of small group video calls
    column_filter.append('choice_prefer')                # Preferences for who chooses WFH days
    column_filter.append('coworkers_samedays_pref')      # Preferences coworkers same WFH days
    column_filter.append('wfh_extraeff_comm_quant')      # How much of your extra efficiency is due to commuting savings
    column_filter.append('prom_eff_1day_quant')          # How much would your chance of promotion be affected by +1 day of WFH
    column_filter.append('client_interactions')          # Do you like interacting with clients
    column_filter.append('coworker_interactions')        # Do you like interacting with coworkeres
    column_filter.append('wfh_coordinate_pref')          # Would you prefer to coordinate or not
    column_filter.append('wfh_coordinate_eff')           # Would coordinating make you more efficient
 
    # Commuting Variables
    column_filter.append('commutetime_quant')            # Commute time (mins)
    column_filter.append('commutemode')                  # Commute mode 2019
    column_filter.append('commutemode_s')                # Commute mode 2019 (simplified)
    column_filter.append('drivealone_preCOVID_pct')      # Commute drive % in 2019
    column_filter.append('carpool_preCOVID_pct')         # Commute carpool % in 2019
    column_filter.append('publictr_preCOVID_pct')        # Commute PT % in 2019
    column_filter.append('bicycle_preCOVID_pct')         # Commute bike % in 2019
    column_filter.append('walk_preCOVID_pct')            # Commute walk % in 2019
    column_filter.append('taxi_preCOVID_pct')            # Commute taxi % in 2019
    column_filter.append('nocommute_preCOVID_pct')       # Commute none % in 2019
    column_filter.append('drivealone_current_pct')       # Commute drive % now
    column_filter.append('carpool_current_pct')          # Commute carpool % now
    column_filter.append('publictr_current_pct')         # Commute PT % now
    column_filter.append('bicycle_current_pct')          # Commute bike % now
    column_filter.append('walk_current_pct')             # Commute walk % now
    column_filter.append('taxi_current_pct')             # Commute taxi % now
    column_filter.append('nocommute_current_pct')        # Commute none % now
    column_filter.append('leavetime_preCOVID')           # Departure time 2019
    column_filter.append('leavetime_current')            # Departure time % now
    column_filter.append('leavetime_preCOVID_quant')     # Departure time 2019
    column_filter.append('leavetime_current_quant')      # Departure time % now
    column_filter.append('commute_mode_faf')             # Commute mode for FAF
    column_filter.append('commute_mode_cowork')          # Commute mode for coworking
    column_filter.append('commute_mode_public')          # Commute mode for public
    column_filter.append('commutetime_to_faf')           # Commute time to FAF
    column_filter.append('commutetime_to_cowork')        # Commute time to FAF
    column_filter.append('commutetime_to_public')        # Commute time to FAF
    column_filter.append('commutetime_from_faf')         # Commute time from FAF
    column_filter.append('commutetime_from_cowork')      # Commute time from FAF
    column_filter.append('commutetime_from_public')      # Commute time from FAF
    column_filter.append('freq_nonwork_car')             # Frequency of mode for non-work trips
    column_filter.append('freq_nonwork_taxi')            # Frequency of mode for non-work trips
    column_filter.append('freq_nonwork_transit')         # Frequency of mode for non-work trips
    column_filter.append('freq_nonwork_bike')            # Frequency of mode for non-work trips
    column_filter.append('freq_nonwork_walk')            # Frequency of mode for non-work trips
    
    # Home Variables
    column_filter.append('zipcode_live_current')         # Home zip code
    column_filter.append('censusdivision')               # Census division (broad region of USA)
    column_filter.append('redstate')                     # Red state indicator 
    column_filter.append('logpop_den_Feb20')             # PreCOVID home popden
    column_filter.append('logpop_den_current')           # Current home popden
    column_filter.append('wfh_ownroom_notbed')           # Home office?
    column_filter.append('live_children')                # Parent?
    column_filter.append('live_adults')                  # Live with adults?
    column_filter.append('internet_quality_quant')       # Home internet quality
    column_filter.append('wfh_invest_burs')              # Investment in WFH equipment that was reimbursed
    column_filter.append('wfh_invest_quant')             # Investment in WFH equipment total
    
    # Work Variables
    column_filter.append('work_industry')                # Industry
    column_filter.append('occupation')                   # Occupation
    column_filter.append('self_employment')              # Self employed
    column_filter.append('employer_sizecat')             # Company size
    column_filter.append('workteam_tasks_percent')       # Percent collaboration
    column_filter.append('workteam_npeople')             # Size of team
    column_filter.append('zipcode_job_current')          # Job zip code
    column_filter.append('logpop_den_job_preCOVID')      # PreCOVID job popden
    column_filter.append('logpop_den_job_current')       # Current job popden
    column_filter.append('worksite_option')              # Option to work in multiple places?
    column_filter.append('worktime_remoteable_pct')      # Percent of work that can be done remote
    column_filter.append('worktime_nonremoteable_pct')   # Percent of work that cannot be done remote
    column_filter.append('worktime_nonremotable_why')    # Why not 100% to above?
    column_filter.append('worktime_nonremotable_f2fcl')  # Not 100% due to clients
    column_filter.append('worktime_nonremotable_f2fco')  # Not 100% due to colleagues
    column_filter.append('worktime_nonremotable_equip')  # Not 100% due to equipment
    column_filter.append('worktime_nonremotable_other')  # Not 100% for other reason
    column_filter.append('who_sets_wfhsched')            # Who sets wfh sched?
    column_filter.append('who_decides_wfhdays')          # Who decides which days?
    column_filter.append('wfhcovid_fracmat')             # Last week WFH %
    column_filter.append('work_facility')                # Work facility type
    column_filter.append('work_computer_pct')            # Percentage of work using computer
    column_filter.append('workhours_duringCOVID')        # Number of working hours during week of survey
    column_filter.append('meetings_workday_pct')         # Percentage of work in meetings
    column_filter.append('meetings_cow_pct')             # Percentage of work in meetings with coworkers
    column_filter.append('boss_plan_implement')          # Are you following your boss' plans
    column_filter.append('boss_wfh_samedays')            # Are you following your boss' plans
    column_filter.append('boss_wfh_unravel')             # What would you do if boss started coming in
    column_filter.append('coworkers_wfh_unravel')        # What would you do if coworkers started coming in
    column_filter.append('employer_days_meet')           # Are you following your boss' plans
    column_filter.append('common_varying_sched')         # What type of policy do you have?

    # WFH Variables
    column_filter.append('wfhcovid_frac')                     # WFH % last week
    column_filter.append('numwfh_days_postCOVID_s_u')         # WFH % desired
    column_filter.append('numwfh_days_postCOVID_boss_s_u')    # WFH % planned
    column_filter.append('wfh_able_qual')                     # Able to WFH any amount?
    column_filter.append('wfh_dow_preferM')                   # Prefer Monday
    column_filter.append('wfh_dow_preferT')                   # Prefer Tuesday
    column_filter.append('wfh_dow_preferW')                   # Prefer Wednesday
    column_filter.append('wfh_dow_preferR')                   # Prefer Thursday
    column_filter.append('wfh_dow_preferF')                   # Prefer Friday
    column_filter.append('wfh_dow_preferNA')                  # No preference
    column_filter.append('worktime_curr_home_pct')            # Current % of time at HOME
    column_filter.append('worktime_curr_ebp_pct')             # Current % of time at OFFICE
    column_filter.append('worktime_curr_client_pct')          # Current % of time at CLIENT
    column_filter.append('worktime_curr_faf_pct')             # Current % of time at FAF
    column_filter.append('worktime_curr_cowork_pct')          # Current % of time at COWORK
    column_filter.append('worktime_curr_public_pct')          # Current % of time at PUBLIC
    column_filter.append('worktime_des_home_pct')             # Desired % of time at HOME
    column_filter.append('worktime_des_ebp_pct')              # Desired % of time at OFFICE
    column_filter.append('worktime_des_client_pct')           # Desired % of time at CLIENT
    column_filter.append('worktime_des_faf_pct')              # Desired % of time at FAF
    column_filter.append('worktime_des_cowork_pct')           # Desired % of time at COWORK
    column_filter.append('worktime_des_public_pct')           # Desired % of time at PUBLIC
    column_filter.append('worktime_des_nowork')               # Desired % of time not working
    column_filter.append('worktime_plan_home_pct')            # Employer % of time at HOME
    column_filter.append('worktime_plan_ebp_pct')             # Employer % of time at OFFICE
    column_filter.append('worktime_plan_client_pct')          # Employer % of time at CLIENT
    column_filter.append('worktime_plan_faf_pct')             # Employer % of time at FAF
    column_filter.append('worktime_plan_cowork_pct')          # Employer % of time at COWORK
    column_filter.append('worktime_plan_public_pct')          # Employer % of time at PUBLIC
    column_filter.append('worktime_plan_nowork')              # Employer % of time not working
    
    # Attention Checks
    column_filter.append('sum3plus4')                     # Attention check = 7
    column_filter.append('cities_attn')                   # Attention check = 33
    column_filter.append('grass_color_attnfull')          # Attention check = Purple or Green
    
    # Weights
    column_filter.append(scale_col)                       # Scale column
    df = dataset.filter(column_filter)
    
    # Data cleaning
    df = df.rename(columns={scale_col: "scale"})
    df = df[(df['cities_attn'] == 33) | (df['cities_attn'].isna())]
    return df

# Returns column with data assigned to bins
def bin_column(target_col, bins, bin_labels = None):    
    return pd.cut(target_col, bins, labels=bin_labels)

# Returns column name with largest value from a set of columns
def get_primary(df, target_cols):
    filt_df = df.filter(target_cols).dropna()
    return filt_df.idxmax(axis = 'columns')

# Returns a column with replaced values based on input
def replace_values(target_col, conversion_dict):
    return target_col.replace(conversion_dict)

# Returns indicator column for one or two equality/membership conditions. "Op" can be le (<=) or ge (>=)
def indicator_column_ineq(df, filtcol1, filtvals1, op1, filtcol2=None, filtvals2=None, op2=None):
    if filtcol2 == None:
        bool_col = op1(df[filtcol1], filtvals1)
    else:
        bool_col = op1(df[filtcol1], filtvals1) & op2(df[filtcol2], filtvals2)
    return bool_col.astype(int)

# Returns indicator column for one or two equality conditions
def indicator_column_eq(df, filtcol1, filtval1, filtcol2=None, filtval2=None):
    if filtcol2 == None:
        bool_col = df[filtcol1] == filtval1
    else:
        bool_col = (df[filtcol1] == filtval1) & (df[filtcol2] == filtval2)
    return bool_col.astype(int)

# Creates new columns that combine or bin existing columns.
def create_columns(df):
    # Combine sustainable modes and third places into new columns
    df['susmode_curr'] = df['publictr_current_pct'] + df['bicycle_current_pct'] + df['walk_current_pct'] + df['carpool_current_pct']
    df['third_curr'] = df['worktime_curr_faf_pct'] + df['worktime_curr_cowork_pct'] + df['worktime_curr_public_pct']
    df['ebp_client'] = df['worktime_curr_ebp_pct'] + df['worktime_curr_client_pct']
    
    df['third_des'] = df['worktime_des_faf_pct'] + df['worktime_des_cowork_pct'] + df['worktime_des_public_pct']
    
    # Get difference between third place actual and third place desired (if positive)
    df['third_diff'] = df['third_des'] - df['third_curr']
    df.loc[df['third_diff'] < 0, 'third_diff'] = 0
    
    # Count weekly number of nonwork trips
    df['nonwork_count'] = replace_values(df['freq_nonwork_bike'], {1:5, 2:3, 3:1, 4:0}) + replace_values(df['freq_nonwork_car'], {1:5, 2:3, 3:1, 4:0}) + replace_values(df['freq_nonwork_taxi'], {1:5, 2:3, 3:1, 4:0}) + replace_values(df['freq_nonwork_transit'], {1:5, 2:3, 3:1, 4:0}) + replace_values(df['freq_nonwork_walk'], {1:5, 2:3, 3:1, 4:0})                                        
    df['wfh_percep_quant'] = replace_values(df['freq_nonwork_bike'], {1:5, 2:3, 3:1, 4:0}) + replace_values(df['freq_nonwork_car'], {1:5, 2:3, 3:1, 4:0}) + replace_values(df['freq_nonwork_taxi'], {1:5, 2:3, 3:1, 4:0}) + replace_values(df['freq_nonwork_transit'], {1:5, 2:3, 3:1, 4:0}) + replace_values(df['freq_nonwork_walk'], {1:5, 2:3, 3:1, 4:0})                                        
    
    # Create indicator column for switch from sustainable to non-sustainable and vice-versa
    df['susmode_preCOVID'] = df['publictr_preCOVID_pct'] + df['bicycle_preCOVID_pct'] + df['walk_preCOVID_pct'] + df['carpool_preCOVID_pct']
    df['sus_switch'] = indicator_column_ineq(df, 'susmode_preCOVID', 50, le, filtcol2='susmode_curr', filtvals2=50, op2=ge) * 100
    df['nonsus_switch'] = indicator_column_ineq(df, 'susmode_preCOVID', 50, ge, filtcol2='susmode_curr', filtvals2=50, op2=le) * 100
    
    # Create primary work location, mode, trip count, third count (3rd place only) columns
    df['top_loc'] = get_primary(df, ['worktime_curr_home_pct', 'worktime_curr_client_pct', 'worktime_curr_ebp_pct', 
                                 'worktime_curr_faf_pct', 'worktime_curr_cowork_pct', 'worktime_curr_public_pct'])
    df['top_mode'] = get_primary(df, ['drivealone_current_pct', 'carpool_current_pct', 'publictr_current_pct', 
                                      'bicycle_current_pct', 'walk_current_pct', 'taxi_current_pct', 'nocommute_current_pct'])
    
    # Create columns for different working arrangements
    df['home_only'] = indicator_column_eq(df, 'worktime_curr_home_pct', 100)
    df['ebp_home_only'] = indicator_column_eq(df, 'third_curr', 0)
    df['home_third'] = indicator_column_ineq(df, 'worktime_curr_home_pct', 0.1, ge, filtcol2='third_curr', filtvals2=0.1, op2=ge)
    df['ebp_home_third'] = indicator_column_ineq(df, 'home_third', 0.1, ge, filtcol2='ebp_client', filtvals2=0.1, op2=ge)
    df['ebp_third'] = indicator_column_ineq(df, 'third_curr', 0.1, ge, filtcol2='ebp_client', filtvals2=0.1, op2=ge)
    df['ebp_home_public'] = indicator_column_ineq(df, 'ebp_home_third', 0.1, ge, filtcol2='worktime_curr_public_pct', filtvals2=0.1, op2=ge)
    df['ebp_home_cowork'] = indicator_column_ineq(df, 'ebp_home_third', 0.1, ge, filtcol2='worktime_curr_cowork_pct', filtvals2=0.1, op2=ge)
    df['ebp_home_faf'] = indicator_column_ineq(df, 'ebp_home_third', 0.1, ge, filtcol2='worktime_curr_faf_pct', filtvals2=0.1, op2=ge)

    
    df['some_public'] = indicator_column_ineq(df, 'worktime_curr_public_pct', 0.1, ge, )
    df['some_cowork'] = indicator_column_ineq(df, 'worktime_curr_cowork_pct', 0.1, ge)
    df['some_faf'] = indicator_column_ineq(df, 'worktime_curr_faf_pct', 0.1, ge)
    df['some_third'] = indicator_column_ineq(df, 'third_curr', 0.1, ge)
    
    # Get total commuting times
    df['comtime_faf_total'] = df['commutetime_to_faf'] + df['commutetime_from_faf']
    df['comtime_cowork_total'] = df['commutetime_to_cowork'] + df['commutetime_from_cowork']
    df['comtime_public_total'] = df['commutetime_to_public'] + df['commutetime_from_public']
    
    # Create bin column for percentage questions
    bins = np.arange(-10, 101, 10).tolist()
    df['remoteable_bins'] = bin_column(df['worktime_remoteable_pct'], bins, bins[1:])
    df['nonremoteable_bins'] = bin_column(df['worktime_nonremoteable_pct'], bins, bins[1:])
    df['compuse_bins'] = bin_column(df['work_computer_pct'], bins, bins[1:])
    df['collaboration_bins'] = bin_column(df['workteam_tasks_percent'], bins, bins[1:])
    df['third_curr_bins'] = bin_column(df['third_curr'], bins, bins[1:])
    df['comtime_bins'] = bin_column(df['commutetime_quant'], bins, bins[1:])
    df['comtime_faf_bins'] = bin_column(df['comtime_faf_total'], bins, bins[1:])
    df['comtime_public_bins'] = bin_column(df['comtime_public_total'], bins, bins[1:])
    df['comtime_cowork_bins'] = bin_column(df['comtime_cowork_total'], bins, bins[1:])
    df['comtime_efficiency_bins'] = bin_column(df['wfh_extraeff_comm_quant'], bins, bins[1:])
    df['meetings_workday_bins'] = bin_column(df['meetings_workday_pct'], bins, bins[1:])
    df['meetings_cow_bins'] = bin_column(df['meetings_cow_pct'], bins, bins[1:])
    df['wfh_invest_burs_bins'] = bin_column(df['wfh_invest_burs'], bins, bins[1:])
    
    bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 750, 1000, 2000, 10000]
    df['wfh_invest_quant_bins'] = bin_column(df['wfh_invest_quant'], bins, bins[1:])

    bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 100]
    df['teamsize_bins'] = bin_column(df['workteam_npeople'], bins, bins[1:])
    
    bins = np.arange(-60, 101, 10).tolist()
    df['wfh_eff_COVID_bins'] = bin_column(df['wfh_eff_COVID_quant'], bins, bins[1:])
    
    bins = np.arange(-110, 101, 20).tolist()
    df['prom_eff_bins'] = bin_column(df['prom_eff_1day_quant'], bins, bins[1:])

    bins = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 80, 100]
    df['workhours_bins'] = bin_column(df['workhours_duringCOVID'], bins, bins[1:])

    # Convert home and work density into categories
    bins = [0, np.log(1000), np.log(3000), 12]
    df['home_pop_category'] = bin_column(df['logpop_den_current'], bins, ['Rural', 'Suburban', 'Urban'])
    df['work_pop_category'] = bin_column(df['logpop_den_job_current'], bins, ['Rural', 'Suburban', 'Urban'])
    
    # Find the average level of fear on shared/active modes
    bins = [-2, -1, 0, 1, 2, 3, 4]
    df['avgfear'] = df[['infectionfear_subway', 'infectionfear_train', 'infectionfear_bus', 'infectionfear_bikewalk']].mean(axis=1)
    df['avgfear_bins'] = bin_column(df['avgfear'], bins, ['N/A', '0', '1', '2', '3', '4'])
    
    bins = [-1, 0, 10, 15, 20, 25]
    df['third_curr_bins_small'] = bin_column(df['third_curr'], bins, bins[1:])

    
    bins = np.arange(-20, 101, 20).tolist()
    df['wfh_curr_bins'] = bin_column(df['wfhcovid_fracmat'], bins, bins[1:])
    
    # Resolve issue with different response categories for preCOVID and current leave time questions
    df['leavetime_current_quant_adj'] = replace_values(df['leavetime_current_quant'], {11.5 : 11.0})
    
    # Replace counterintuitive category tags
    df['worksite_option'] = replace_values(df['worksite_option'], {2.0: 0, 1.0: 1})
    
    # Hours worked by location (divide pct var by 100)
    df['ebp_hours'] = df['worktime_curr_ebp_pct'].multiply(df['workhours_duringCOVID'], axis='index') / 100
    df['client_hours'] = df['worktime_curr_client_pct'].multiply(df['workhours_duringCOVID'], axis='index') / 100
    df['faf_hours'] = df['worktime_curr_faf_pct'].multiply(df['workhours_duringCOVID'], axis='index') / 100 
    df['cowork_hours'] = df['worktime_curr_cowork_pct'].multiply(df['workhours_duringCOVID'], axis='index') / 100
    df['public_hours'] = df['worktime_curr_public_pct'].multiply(df['workhours_duringCOVID'], axis='index') / 100

    return df

# Return dataset filtered to a particular date range
def date_filter(df, start_date = '2019-01-01', end_date = '2024-01-01'):
    filtered_df = df[df['date'] >= start_date]
    filtered_df = filtered_df[filtered_df['date'] <= end_date]
    return filtered_df

# Return variable scaled using scale column (and the sum of the scale values)
def scale_var(input_df, target_col):
    df = pd.DataFrame()
    df['var'] = input_df[target_col]
    df['scale'] = input_df['scale']
    df['date'] = input_df['date']
    df = df.dropna() # Remove NA values
    scale_sum = sum(df.scale)
    scale_var = df['var'].multiply(df['scale'], axis='index')
    print("Sample size: " + str(len(df)))
    return [scale_var, scale_sum]

# Return weighted average of an entire column
def weighted_avg(df, target_col):
    scaled_var = scale_var(df, target_col)
    return sum(scaled_var[0]) / scaled_var[1]

# Return a dictionary with the counts of the specified variable by category
def count_var(target_col): 
    return target_col.value_counts().to_dict()

# Return a dictionary with the sum of each variable by category
def sum_var(target_col):
    return target_col.groupby(target_col).sum().to_dict()

# Return the list of categories for input variable
def get_categories(target_col):
    return list(set(target_col))

# Returns dates with valid answers for input variable
def get_dates(df, target_col):
    date_df = df.dropna(subset=[target_col])
    return sorted(list(set(date_df.date)))

# Returns column filtered by up to two column values
def filter_in(df, target_col, filtcol1, filtvals1, filtcol2=None, filtvals2=None):
    if filtcol2 == None:
        df = df[df[filtcol1].isin(filtvals1)]
    else: 
        df = df[df[filtcol1].isin(filtvals1) & df[filtcol2].isin(filtvals2)]
    return df[target_col].dropna()

# Returns weighted values split by month
def weighted_month(df, target_col):
    df_new = df.filter(['date', 'scale', target_col]).dropna()
    df_new['weighted'] = df_new[[target_col]].multiply(df_new['scale'], axis='index')
    df_wt = df_new.groupby('date')[['weighted', 'scale']].sum()
    print("Sample size: " + str(len(df_new)))
    return df_wt['weighted'] / df_wt['scale']

# Returns weighted values split by month
def weighted_avg_group(df, target_col, group_col):
    df_new = df.filter([group_col, 'scale', target_col, 'date']).dropna()
    print("Sample size: " + str(len(df_new)))
    df_new['weighted'] = df_new[[target_col]].multiply(df_new['scale'], axis='index')
    df_wt = df_new.groupby(group_col)[['weighted', 'scale']].sum()
    return df_wt['weighted'] / df_wt['scale']

# Returns weighted frequency of response categories for a specific question
def weighted_freq(df, target_col):
    df_new = df.filter(['scale', target_col, 'date']).dropna()
    print("Sample size: " + str(len(df_new)))
    return df_new.groupby(target_col)['scale'].sum() / df_new.scale.sum()

# Returns as filtered df based on indices of a different series or df
def index_filter(df, filter_obj):
    return df[df.index.isin(filter_obj.index)]

# Returns a dataframe with thirdplace splits for a given category
def thirdplace_split(df, target_col):
    cowork = weighted_avg_group(df, 'worktime_curr_cowork_pct', target_col)
    public = weighted_avg_group(df, 'worktime_curr_public_pct', target_col)
    faf = weighted_avg_group(df, 'worktime_curr_faf_pct', target_col)
    wt_res = pd.concat([cowork, public, faf], axis=1)
    wt_res.columns = ['Coworking Space', 'Public Space', 'Friend+Family']
    return wt_res

# Plots a timeseries line graph for the input variable
def plot_timeseries(data, xlabel=None, ylabel=None, ylim=[None, None], rotate=0, ax=None, datalabel=None):
    if ax == None:
        fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(data.index, data, label=datalabel)
    ax.set_ylim(ylim[0], ylim[1])
    ax.set_axisbelow(True)
    ax.grid(axis='y', linewidth=0.5, color='#DDDDDD', zorder=0)
    ax.grid(axis='y', which='minor', color='#EEEEEE', linewidth=0.3, zorder=0)
    ax.minorticks_on()
    ax.tick_params(axis='x', which='minor', bottom=False)
    ax.tick_params(axis='x', labelrotation = rotate)
    plt.tight_layout()  # otherwise the right y-label is slightly clipped
    if ax != None:
        return ax

# Plots a column chart of the input variable
def plot_column(xdata, ydata, xlabel=None, ylabel=None, ylim=[None, None], xlim=[None,None], 
                width=0.4, blabels=None, rotate=0, ax = None):
    if ax == None:
        fig, ax = plt.subplots()
    ax.bar(xdata, ydata, width=width, edgecolor = "black", linewidth=0.5, align='center')  
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if blabels != None:
        ax.set_xticks(xdata, blabels, rotation=rotate)
    ax.set_ylim(ylim[0], ylim[1])
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_axisbelow(True)
    ax.grid(axis='y', linewidth=0.5, color='#DDDDDD', zorder=0)
    ax.grid(axis='y', which='minor', color='#EEEEEE', linewidth=0.3, zorder=0)
    ax.minorticks_on()
    ax.tick_params(axis='x', which='minor', bottom=False)
    plt.tight_layout()  # otherwise the right y-label is slightly clipped
    if ax != None:
        return ax

# Plots a stacked column chart of the input variable
def plot_stacked_column(df, xlabel=None, ylabel=None, ylim=[None, None], xlim=[None,None], 
                        width=0.4, blabels=None, ax=None, string=False, integer=False):
    if ax == None:
        fig, ax = plt.subplots()
    
    if blabels == None:
        labels = df.index
    else:
        labels = blabels
    
    cols = df.columns
    bottom = np.zeros(len(labels))
    for col in cols:
        if string:
            ax.bar([str(i) for i in labels], list(df[col]), width=width, label = str(col), edgecolor = "black", linewidth=0.5, align='center', bottom=bottom)
        elif integer:
            ax.bar([int(i) for i in labels], list(df[col]), width=width, label = str(col), edgecolor = "black", linewidth=0.5, align='center', bottom=bottom)
        else: 
            ax.bar(labels, list(df[col]), width=width, label = str(col), edgecolor = "black", linewidth=0.5, align='center', bottom=bottom)
        bottom += list(df[col])
        
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(ylim[0], ylim[1])
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_axisbelow(True)
    ax.grid(axis='y', linewidth=0.5, color='#DDDDDD', zorder=0)
    ax.grid(axis='y', which='minor', color='#EEEEEE', linewidth=0.3, zorder=0)
    ax.minorticks_on()
    ax.tick_params(axis='x', which='minor', bottom=False)
    ax.legend()
    if ax != None:
        return ax

# Plots a stacked column chart of the input variable
def plot_clustered_column(df, xlabel=None, ylabel=None, ylim=[None, None], xlim=[None,None], 
                        width=None, blabels=None, rotate=0, ax=None):
    if ax == None:
        fig, ax = plt.subplots(constrained_layout=True)
    if blabels == None:
        labels = df.index
    else:
        labels = blabels

    if width == None:
        width = 0.8/len(df.columns)
    
    multiplier = 0
    x = np.arange(len(labels)) 
    cols = df.columns
    for col in cols:
        offset = width * multiplier
        ax.bar(x+offset, list(df[col]), width=width, label= str(col), edgecolor = "black", linewidth=0.5, align='center')
        multiplier += 1
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(ylim[0], ylim[1])
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_xticks(x + (len(df.columns)-1)/2*width, labels)
    ax.set_axisbelow(True)
    ax.grid(axis='y', linewidth=0.5, color='#DDDDDD', zorder=0)
    ax.grid(axis='y', which='minor', color='#EEEEEE', linewidth=0.3, zorder=0)
    ax.minorticks_on()
    ax.tick_params(axis='x', which='minor', bottom=False)
    ax.legend()
    if ax != None:
        return ax

# Plots a area chart of the input variable
def plot_area(df, xlabel=None, ylabel=None, blabels=None, rotate=0, bbox=[1.3, 0.5]):
    
    # Rearrange input data
    if blabels == None: blabels = df.columns
    yvals = {}
    for index, column in enumerate(df):
        coldata = df[column]
        yvals[blabels[index]] = list(coldata)
    
    fig, ax1 = plt.subplots()
    ax1.stackplot(list(df.index), yvals.values(), labels=yvals.keys(),
                    linewidth=0.5, edgecolor='black')
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.set_ylim(0, 100)
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    ax1.legend(loc="center right",  bbox_to_anchor=(bbox[0], bbox[1]))
    return ax1

# Plots a pie chart of the input variables
def plot_pie(data, labels, title=None):
    colors = iter([plt.cm.Pastel1(i) for i in range(20)])
    fig, ax1 = plt.subplots()
    ax1.pie(data, labels=labels, colors=colors, autopct='%.1f%%', pctdistance=0.8)
    ax1.axis('equal')
    plt.title(title)
    wedges = [patch for patch in ax1.patches if isinstance(patch, mpl.patches.Wedge)]
    for w in wedges:
        w.set_linewidth(0.5)
        w.set_edgecolor('black')
    return ax1

# Create dictionary to store common category labels
def label_dict():
    ld = {}
    ld['income'] = ['<20','25','35','45','55','65','75','90','115','135','175','225', '500', '1M+']
    ld['industry'] = ['Agri', 'Arts', 'Finance', 'Constr', 'Ed', 'Health', 'Hospitality/Food', 'Info', 'Manufac', 'Mining', 
                      'Prof/Bus. Serv.', 'RE', 'Retail', 'Transport', 'Util', 'Wholesale', 'Govt', 'Other']
    ld['occupation'] = ['Military', 'Construction', 'Farm/Forest', 'Maintenance', 'Mgmt/Bus/Finance', 'Admin', 'Production', 
                        'Professional', 'Sales', 'Service', 'Transport', 'Other']
    ld['emp_size'] = ['<10', '10-50', '50-100', '100-500', '500+']
    ld['work_loc'] = ['Home', 'Client', 'Office', 'FFH', 'Cowork', 'Public']
    ld['educ'] = ['<HS', 'HS', 'Some Col', 'Bach', 'Mast', 'PhD']
    ld['agebin'] = ['Under 30', '30-39', '40-49', '50+']
    ld['modes'] = ['Drive', 'Carpool', 'Transit', 'Bike', 'Walk', 'Taxi', 'None']
    ld['censusdiv'] = ['NE', 'MA', 'ENC', 'WNC', 'SA', 'ESC', 'WSC', 'Mtn', 'Pac']
    ld['whosets'] = ['Me', 'Team', 'Org.', 'Varies', 'Not clear', 'Other']

    return ld














