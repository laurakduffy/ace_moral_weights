import squigglepy as sq
from squigglepy.numbers import K, M, B
import numpy as np


SIMULATIONS = 10000


def print_results(animal_name, alive_any_point):
    percentiles = sq.get_percentiles(alive_any_point, [0.15, 5, 50, 95, 99.85])
    mean = np.mean(alive_any_point)
    print(animal_name)
    print(percentiles)
    print(mean)

def farmed_shrimp_years_lived_per_year():
    # from Daniela Waldhorn's Shrimp scoping report
    larval_wts = [98/240, 14/240, 23/240, 100/240, 1-98/240-14/240-23/240-100/240]
    days_lived_shrimp_die_larval = sq.mixture([sq.lognorm(0.5, 9, lclip=0.4), sq.lognorm(0.5, 9.5, lclip=0.4), \
        sq.lognorm(0.5, 12, lclip=0.4), sq.lognorm(2, 30, lclip=0.5), sq.lognorm(0.5, 30, lclip=0.4)], \
        larval_wts)
    number_die_larval = 240*B

    postlarval_wts = [84/120, 10/120, 8/120, 15/120, 1-84/120-10/120-8/120-15/120]
    days_lived_shrimp_die_postlarval = sq.mixture([sq.lognorm(11, 20, lclip=5), sq.lognorm(11, 26, lclip=5), \
        sq.lognorm(18, 65, lclip=5), sq.lognorm(30, 60, lclip=10), sq.lognorm(16, 86, lclip=5)], \
        postlarval_wts)
    number_die_postlarval = 120*B

    juvenile_wts = [100/160, 9.6/160, 10/160, 32/160, 1-100/160-9.6/160-10/160-32/160]
    days_lived_shrimp_die_juvenile = sq.mixture([sq.lognorm(53, 110, lclip=20), sq.lognorm(35, 150, lclip=15), \
        sq.lognorm(41, 120, lclip=20), sq.lognorm(60, 150, lclip=20), sq.lognorm(26, 200, lclip=10)], \
        juvenile_wts)
    number_die_juvenile = 160*B

    adult_wts = [360/440, 22/440, 24/440, 32/440, 1-360/440-22/440-24/440-32/440]
    days_lived_shrimp_die_adult = sq.mixture([sq.norm(110, 210), sq.norm(140, 210), \
        sq.norm(120, 190), sq.norm(140, 250), sq.norm(88, 270)], \
        adult_wts)
    number_die_larval = 440*B

    shrimp_years_lived_per_year = (days_lived_shrimp_die_larval*number_die_larval + days_lived_shrimp_die_postlarval*number_die_postlarval + \
        days_lived_shrimp_die_juvenile*number_die_juvenile + days_lived_shrimp_die_adult*number_die_larval)/365
    
    arr_shrimp_alive_any_time = sq.sample(shrimp_years_lived_per_year, SIMULATIONS)

    return arr_shrimp_alive_any_time

def cochineals_alive_any_time():
    adult_fem_killed = sq.norm(4*B, 18*B, lclip=1*B, rclip=22*B)
    lifespan_adult_fem = sq.norm(0.2, 0.25, lclip=0.15, rclip=0.3)

    males_killed = sq.norm(3000*B, 14000*B, lclip=1000*B, rclip=16000*B)
    lifespan_males = sq.norm(0.01, 0.02, lclip=0.005, rclip=0.03)

    f_nymph_killed = sq.norm(1500*B, 7300*B, lclip=500*B, rclip=10000*B)
    lifespan_f_nymph = sq.norm(0.01, 0.02, lclip=0.005, rclip=0.03)

    adult_female_yrs = adult_fem_killed*lifespan_adult_fem
    males_yrs = males_killed*lifespan_males
    f_nymph_yrs = f_nymph_killed*lifespan_f_nymph

    cochineals_alive = adult_female_yrs + males_yrs + f_nymph_yrs

    arr_cochineals_alive = sq.sample(cochineals_alive, SIMULATIONS)

    return arr_cochineals_alive

def bsf_alive_any_time():
    num_per_year = sq.norm(0.5*B, 1.5*B, lclip=0.1*B, rclip=2*B)
    lifespan = sq.norm(0.05, 0.15, lclip=0.025, rclip=0.0175)

    bsf_alive_any_point = num_per_year*lifespan

    arr_bsf_alive_any_point = sq.sample(bsf_alive_any_point, SIMULATIONS)

    return arr_bsf_alive_any_point

def mealworm_alive_any_time():
    num_per_year = sq.norm(50*B, 500*B, lclip=10*B, rclip=600*B)
    lifespan = sq.norm(0.15, 0.25, lclip=0.1, rclip=0.3)

    mealworm_alive_any_point = num_per_year*lifespan

    arr_mealworm_alive_any_point = sq.sample(mealworm_alive_any_point, SIMULATIONS)

    return arr_mealworm_alive_any_point

def amphibians_reptiles_any_time():
    frogs = sq.lognorm(120*M, 2.6*B, lclip=100*M, rclip=3*B)
    chinese_turtles = sq.lognorm(250*M, 2.1*B, lclip=200*M, rclip=2.5*B)

    alive_any_time = frogs + chinese_turtles
    arr_alive_any_time = sq.sample(alive_any_time, SIMULATIONS)
    return arr_alive_any_time

def chickens_any_time():
    hens = sq.norm(6.8*B, 9.9*B, lclip=5*B, rclip=12*B)
    broilers = sq.norm(9.5*B, 16.2*B, lclip=7*B, rclip=20*B)
    meat_mothers = sq.norm(350*M, 600*M, lclip=200*M, rclip=800*M)
    meat_fathers = sq.norm(40*M, 70*M, lclip = 20*M, rclip=90*M)
    
    chickens_alive = hens + broilers + meat_mothers + meat_fathers
    arr_chickens_alive = sq.sample(chickens_alive, SIMULATIONS)

    return arr_chickens_alive

def lab_animals_any_time():
    total_per_year = sq.norm(150*M, 230*M, lclip=100*M, rclip=280*M)
    percent_exempt = sq.uniform(0.1, 0.2)
    mammals_per_year = total_per_year*(1-percent_exempt)

    years_lived_per_year = sq.uniform(0.8, 1.0)

    alive_any_time = mammals_per_year*years_lived_per_year

    arr_lab_animals_alive = sq.sample(alive_any_time, SIMULATIONS)
    return arr_lab_animals_alive

lab_animals = lab_animals_any_time()
print_results("lab animals", lab_animals)