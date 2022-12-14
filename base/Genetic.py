import numpy as np
import pandas as pd
import json
import random
from . import Fuzzy as fuzz


# KHOI TAO BO TRONG SO
# physical
physical_1 = np.array([0, 0, 0, 0])
physical_2 = np.array([0, 0, 0, 0])
physical_3 = np.array([0, 0, 0, 0])
physical_4 = np.array([0, 0, 0, 0])
physical_5 = np.array([0, 0, 0, 0])
physical_6 = np.array([0, 0, 0, 0])

physical_weight = [physical_1, physical_2,   
                   physical_3, physical_4,    
                   physical_5, physical_6]
# print("\nThe luc: \n", physical_weight)


# eye sight
eye_1 = np.array([0, 0, 0])
eye_2 = np.array([0, 0, 0])
eye_3 = np.array([0, 0, 0])
eye_4 = np.array([0, 0, 0])
eye_5 = np.array([0, 0, 0])
eye_6 = np.array([0, 0, 0])

eye_weight = [eye_1, eye_2, eye_3, eye_4, eye_5, eye_6]
# print("\nMat: \n", eye_weight)


# tooth decay
tooth_2 = np.array([0, 0, 0])
tooth_3 = np.array([0, 0, 0, 0])
tooth_4 = np.array([0, 0, 0])
tooth_5 = np.array([0, 0, 0])

tooth_weight = [tooth_2, tooth_3, tooth_4, tooth_5]
# print("\nRang: \n", tooth_weight)


# hearing power
hearing_1 = np.array([0, 0, 0, 0])
hearing_2 = np.array([0, 0, 0, 0])
hearing_3 = np.array([0, 0, 0, 0])
hearing_4 = np.array([0, 0, 0, 0])
hearing_5 = np.array([0, 0, 0, 0])
hearing_6 = np.array([0, 0, 0, 0])

hearing_weight = [hearing_1, hearing_2,
                  hearing_3, hearing_4,
                  hearing_5, hearing_6]
# print("\nTai: \n", hearing_weight)


# max blood
blood_1 = np.array([0, 0, 0, 0])
blood_2 = np.array([0, 0, 0, 0])
blood_3 = np.array([0, 0, 0, 0])
blood_4 = np.array([0, 0, 0, 0])
blood_5 = np.array([0, 0, 0, 0])
blood_6 = np.array([0, 0, 0, 0])

blood_weight = np.array([blood_1, blood_2, 
                         blood_3, blood_4, 
                         blood_5, blood_6], dtype = object)
# print("\nMau: \n", blood_weight)


# size Fungal
fungal_2 = np.array([0, 0, 0, 0])
fungal_3 = np.array([0, 0, 0, 0])
fungal_4 = np.array([0, 0, 0, 0])

fungal_weight = np.array([fungal_2, fungal_3, fungal_4], dtype = object)
# print("\nDa: \n", fungal_weight)


# length Difference
length_4 = np.array([0, 0, 0, 0])
length_5 = np.array([0, 0, 0, 0])
length_6 = np.array([0, 0, 0, 0])

length_weight = np.array([length_4, length_5, length_6], dtype = object)
# print("\nChan tay: \n", length_weight)


# health index
health_1 = np.array([0, 0, 0, 0])
health_2 = np.array([0, 0, 0])
health_3 = np.array([0, 0, 0])
health_4 = np.array([0, 0, 0])
health_5 = np.array([0, 0, 0])
health_6 = np.array([0, 0, 0, 0])

health_weight = [health_1, health_2, 
                 health_3, health_4, 
                 health_5, health_6]
# print("\nChi so SK: \n", health_weight)

###########################################################################################################################
###########################################################################################################################

# BO TRONG SO
set_of_weights = [physical_weight, eye_weight, tooth_weight, hearing_weight, blood_weight, fungal_weight, length_weight, health_weight]




















#N???p d??? li???u m???u t??? Excel
def nap_du_lieu_mau():
    
    list = pd.read_excel('C:/Users/ADM/Desktop/HK_9/dulieumau.xlsx', index_col=0, skiprows=1)
    print(list)
    print("-------------------------------------------------------------------------\n\n")
    mylist = list.to_json()
    print(mylist)


    print("-------------------------------------------------------------------------\n\n")
    data = json.loads(mylist)

    count_row = len(data["The_luc"])
    print("count_row        : ", count_row)

    thuoc_tinh = []
    for key, value in data.items():
        data_thuoc_tinh = []
        for index in value:
            data_thuoc_tinh.append(value[index])
        thuoc_tinh.append(data_thuoc_tinh)


    count_column = len(thuoc_tinh)
    print("count_column     : ", count_column)
    print("-------------------------------------------------------------------------\n\n")

        
    sample_datasets = []
    for i in range(count_row):
        tmp = []
        for j in range(count_column):
            tmp.append(thuoc_tinh[j][i])
        sample_datasets.append(tmp)
        
    #D??? li???u m???u    
    print(sample_datasets) 
    
    return sample_datasets




def initialize_population(population, popmax):
    print("KHOI TAO GTDT....")
    for count in range(popmax):
        weights = []
        
        a = fuzz.random_physical_weight(physical_weight)
        b = fuzz.random_eye_weight(eye_weight)
        c = fuzz.random_tooth_weight(tooth_weight)
        d = fuzz.random_hearing_weight(hearing_weight)
        e = fuzz.random_blood_weight(blood_weight)
        f = fuzz.random_fungal_weight(fungal_weight)
        g = fuzz.random_length_weight(length_weight)
        h = fuzz.random_health_weight(health_weight)
        
        weights = [a, b, c, d, e, f, g, h]
        population.append(weights)
        print("+++++++++++++++++++++++++\n")
        
    return population



class Individual_eval:
    def __init__(self, individual, fitness_rate):
        self.individual = individual
        self.fitness_rate = fitness_rate



def calculate_fitness (population, sample_datasets):
    print("CACULATE FITNESS....")
    individuals_evaluated = []
    
    for individual in population:
        
        count = 0
        
        for sample_data in sample_datasets:
            output_fuzzy = fuzz.fuzzy(individual, sample_data)
            
            output_fuzzy_result = output_fuzzy['health_index']
            lower_limit_value = sample_data[7] - 1
            upper_limit_value = sample_data[7] + 1
            
            if (output_fuzzy_result >= lower_limit_value) and (output_fuzzy_result <= upper_limit_value):
                count = count + 1
        
        fitness_rate = count * 0.01
        individuals_evaluated.append(Individual_eval(individual, fitness_rate))
    
    return individuals_evaluated
        
    
def selection(individuals, count):
    print("SELECTION....")
        
    rank = sorted(individuals, key=lambda man: man.fitness_rate, reverse=True)
    
    ranked_selection = []
    
    # L???y 'count' ph???n t??? ?????u ti??n c???a t???p rank
    for individual in rank:
        
        ranked_selection.append(individual.individual)
        
        count = count - 1
        if count == 0:
            break
    
    return ranked_selection
        
        

def crossover(father, mother):
    print("CROSSOVER....")
    midpoint = random.randrange(0, 7, 1)
    
    child = father
    
    for i in range(len(child)):
        if i > midpoint: 
            child[i] = mother[i]
            
    return child     
    
    

def multation(individual, index):
    print("MUTATION....")
    print("//////////////////////////: ", individual)
    if index == 0:
        individual[0] = fuzz.random_physical_weight(individual[0])
    elif index == 1:
        individual[1] = fuzz.random_eye_weight(individual[1])
    elif index == 2:
        individual[2] = fuzz.random_tooth_weight(individual[2])
    elif index == 3:
        individual[3] = fuzz.random_hearing_weight(individual[3])
    elif index == 4:
        individual[4] = fuzz.random_blood_weight(individual[4])
    elif index == 5:
        individual[5] = fuzz.random_fungal_weight(individual[5])
    elif index == 6:
        individual[6] = fuzz.random_length_weight(individual[6])
    else:
        individual[7] = fuzz.random_health_weight(individual[7])
    
    return  individual   


def review (population, sample_datasets):
    print("REVIEW....")
    individuals_evaluated = []
    
    for individual in population:
        
        count = 0
        
        for sample_data in sample_datasets:
            output_fuzzy = fuzz.fuzzy(individual, sample_data)
            
            output_fuzzy_result = output_fuzzy['health_index']
            lower_limit_value = sample_data[7] - 1
            upper_limit_value = sample_data[7] + 1
            
            if (output_fuzzy_result >= lower_limit_value) and (output_fuzzy_result <= upper_limit_value):
                count = count + 1
        
        fitness_rate = count * 0.01 # Chuy???n th??nh c??c gi?? tr???
        
        individuals_evaluated.append(Individual_eval(individual, fitness_rate))
        
        
    rank = sorted(individuals_evaluated, key=lambda individual: individual.fitness_rate, reverse=True)
    
    best_individual = {
        "individual": rank[0].individual,
        "fitness_rate": fitness_rate
    }
    
    return best_individual



































#################################################################
#################################################################

def genetic ():
    
    ## KH???I T???O
    population = []
    popmax = 3
    selectMax = 2
    multation_rate = 0.9
    termination_criteria = 0
    generations = 0
    
    # T???o ra Qu???n th??? g???m 200 c?? th???:
    population = initialize_population(population, popmax)

    print("------------------------------------------")
    print("POPULATION: ", population)
    print("------------------------------------------")
    
    #################################################################
    #################################################################



    
    while(True):
        
        generations = generations + 1
        
        #T??nh to??n Fitness 
            # Input : T???p c??c BTS, b??? d??? li???u m???u (G???m N BTS)
            # Output: T???p c??c (BTS, Eval).
            # Fuzzy ??? ????y
        sample_data = nap_du_lieu_mau()
        individuals_evaluated = calculate_fitness(population, sample_data)

            
            
            
        #L???a ch???n c??c c?? th??? ????? Giao ph???i
            # Input : T???p c??c (BTS, Eval).
            # Output: T???p g???m n BTS c?? eval cao nh???t (n = 20)    
        list_individuals_selected = selection (individuals_evaluated, selectMax)
            
            
            
            
        #Lai gh??p ch??o
            # Input : T???p c??c BTS ???? ???????c L???a ch???n.
            # Output: T???p c??c BTS ???? ???????c Lai gh??p.
            # Solution: 
                # Lai gh??p ch??o c??c ch??? ti??u trong BTS lu??n.
                # T???c l?? gi???a A v?? B s??? ?????i n???a ch??? ti??u lai gh??p cho nhau.
                
        for i in range(len(list_individuals_selected)):
            father_index = random.randrange(1, selectMax, 1)  
            mother_index = random.randrange(1, selectMax, 1)
            
            father = list_individuals_selected[father_index]
            mother = list_individuals_selected[mother_index]
            
            child = crossover(father, mother)
            
            list_individuals_selected[i] = child
            
                    
        
                
        #?????t bi???n
            # Input : T???p c??c BTS ???? ???????c Lai gh??p.
            # Output: T???p c??c BTS ???? ???????c ?????t bi???n.
            # Solution: 
                # B?????c 1: Ch???n random m???t Ch??? Ti??u ????? ?????t bi???n
                    # ?????t bi???n nh?? th??? n??o:
                        # Trong m???t Ch??? Ti??u s??? c?? c??c ??i???m
                        # Trong m???t ??i???m l???i c?? c??c ph???n t??? Number c???a h??m th??nh vi??n.
                        # S??? ?????t bi???n c??c gi?? tr??? n??y b???ng c??ch random gi?? tr??? trong gi???i h???n c???a ch??ng
                        
                # B?????c 2: Duy???t qua c??c ph???n t???, ph???n t??? n??o c?? mutation_rate cao th?? b??? ?????t bi???n
                
        for i in range(len(list_individuals_selected)):
            if(random.random() > multation_rate):
                list_individuals_selected[i] = multation(list_individuals_selected[i], i)
        
        list_individuals_mutation = list_individuals_selected
        
        
        
        
        #Ki???m tra BTS
            # Input : T???p c??c BTS ???? ???????c ?????t bi???n --OR-- T???p BTS kh???i t???o ban ?????u
            # Output: Object {
                        # result : int (1|0)    #(1 l?? ?????t m???c ti??u, 0 l?? kh??ng ?????t m???c ti??u)
                        # BTS    : BTS c?? t??? l??? ch??nh x??c (correct_rate) ?????i v???i B??? d??? li???u m???u l?? cao nh???t;
                        #}
            # Fuzzy ??? ????y
        best_individual = review (list_individuals_mutation, sample_data)
        
        
        # N???u ?????t ch??? ti??u => 
        if best_individual["fitness_rate"] >= termination_criteria:
            perfect_individual = best_individual["individual"]
            break
        else:
            for i in range(popmax):
                population[i] = best_individual["individual"]
    
    form = {
        "perfect_set_of_weights": perfect_individual,
        "generations" : generations
    }
    
    return form