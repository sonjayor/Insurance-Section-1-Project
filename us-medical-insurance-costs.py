#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs
# 

# In[1]:


import csv


# In[2]:


ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


# In[3]:


def load_list_data(first, csv_file, column_name):
    with open('insurance.csv') as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            first.append(row[column_name])
        return first


# In[4]:


load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


# In[5]:


#ESTO ES PARA SACAR LA EDAD PROMEDIO DE TODAS LAS PERSONAS
tsum_age = 0

for age in ages:
    tsum_age += int(age)
    
average_age = tsum_age / len(ages)
    
print("The average age of the patients is " + str(average_age) + " !")


# In[6]:


#ESTO ES PARA SABER CUAL ES EL AREA CON MAS PACIENTES
southwest = 0
southeast = 0
northwest = 0
northeast = 0
all_regions = {}

for i in regions:
    if i == "southwest":
        southwest += 1
    if i == "southeast":
        southeast += 1
    if i == "northwest":
        northwest += 1
    if i == "northeast":
        northeast += 1
        
for info in ["southwest", "southeast", "northwest", "northeast"]:
    all_regions[info] = eval(info)
    
max_value = max(all_regions.values())

max_region = max(all_regions, key=all_regions.get)
    
print("The region with the most patients is " + str(max_region) + " with a total of " + str(max_value) + " patients!")


# In[7]:


#ESTO ES PARA SACAR EL PROMEDIO DE COSTO COMPARANDO FUMADORES Y NO FUMADORES
smokerdic = list(zip(smoker_statuses, insurance_charges))
yessmoker = 0
nosmoker = 0
yescount = smoker_statuses.count('yes')
nocount = smoker_statuses.count('no')

for i, j in smokerdic:
    if i == 'yes':
        yessmoker += float(j)
    if i == 'no':
        nosmoker += float(j)
        
yessmokeravg = yessmoker / yescount
nosmokeravg = nosmoker / nocount
        
print("The average cost per person who does not smoke is: " + str(nosmokeravg) + "!")
print("The average cost per person who smokes is: " + str(yessmokeravg) + "!")
        


# In[8]:


#ESTO ES PARA SACAR EL PROMEDIO DE EDAD DE QUIENES TIENEN HIJOS
withkids = 0

for i in num_children:
    if int(i) > 0:
        withkids += 1
        
ageandkids = list(zip(ages, num_children))
sumages = 0

for i, j in ageandkids:
    if int(j) > 0:
        sumages += int(i)
        
avg_agewkids = sumages / withkids
        
print(avg_agewkids)
    
        


# In[9]:


#ESTO ES PARA SACAR EL PROMEDIO DE COSTO COMPARANDO HOMBRES Y MUJERES
sexescostzip = list(zip(sexes, insurance_charges))
nwomen = sexes.count('female')
nmen = sexes.count('male')
sumcost_women = 0
sumcost_men = 0

for i, j in sexescostzip:
    if i == 'female':
        sumcost_women += float(j)
    if i == 'male':
        sumcost_men += float(j)
        
avgcost_women = sumcost_women / nwomen
avgcost_men = sumcost_men / nmen
    

print("The average cost per woman is: " + str(avgcost_women) + "!")
print("The average cost per man is: " + str(avgcost_men) + "!")


# In[10]:


#ESTO ES PARA SACAR EL PROMEDIO DE COSTO POR PERSONA DEPENDIENDO DE LA CANTIDAD DE HIJOS QUE TENGA

cost_fornumkid = list(zip(num_children, insurance_charges))

zerokid = num_children.count(str(0))
onekid = num_children.count(str(1))
twokid = num_children.count(str(2))
threekid = num_children.count(str(3))
fourkid = num_children.count(str(4))
fivekid = num_children.count(str(5))

sumzerok = 0
sumonek = 0
sumtwok = 0
sumthreek = 0 
sumfourk = 0
sumfivek = 0

for i, j in cost_fornumkid:
    if int(i) == 0:
        sumzerok += float(j)
    if int(i) == 1:
        sumonek += float(j)
    if int(i) == 2:
        sumtwok += float(j)
    if int(i) == 3:
        sumthreek += float(j)
    if int(i) == 4:
        sumfourk += float(j)
    if int(i) == 5:
        sumfivek += float(j)

avgcost_zero = sumzerok / zerokid
avgcost_one = sumonek / onekid
avgcost_two = sumtwok / twokid
avgcost_three = sumthreek / threekid
avgcost_four = sumfourk / fourkid
avgcost_five = sumfivek / fivekid




print("This is the average cost if someone has 0 kid: " + str(avgcost_zero))
print("This is the average cost if someone has 1 kid: " + str(avgcost_one))
print("This is the average cost if someone has 2 kid: " + str(avgcost_two))
print("This is the average cost if someone has 3 kid: " + str(avgcost_three))
print("This is the average cost if someone has 4 kid: " + str(avgcost_four))
print("This is the average cost if someone has 5 kid: " + str(avgcost_five))


# In[11]:


bmi_agesex = list(zip(sexes, ages, bmis))

fem_teenbmisum = 0
fem_twenbmisum = 0
fem_thirbmisum = 0
fem_fortbmisum = 0
fem_fiftybmisum = 0
fem_sixbmisum = 0

male_teenbmisum = 0
male_twenbmisum = 0
male_thirbmisum = 0
male_fortbmisum = 0
male_fiftybmisum = 0
male_sixbmisum = 0

fem_teencount = 0
fem_twencount = 0
fem_thircount = 0
fem_fortcount = 0
fem_fiftycount = 0
fem_sixcount = 0

male_teencount = 0
male_twencount = 0
male_thircount = 0
male_fortcount = 0
male_fiftycount = 0
male_sixcount = 0


for i, j, k in bmi_agesex:
    if i == 'female':
        if int(j) > 17 and int(j) < 20:
            fem_teenbmisum += float(k)
            fem_teencount += 1
        if int(j) > 19 and int(j) < 30:
            fem_twenbmisum += float(k)
            fem_twencount += 1
        if int(j) > 29 and int(j) < 40:
            fem_thirbmisum += float(k)
            fem_thircount += 1
        if int(j) > 39 and int(j) < 50:
            fem_fortbmisum += float(k)
            fem_fortcount += 1
        if int(j) > 49 and int(j) < 60:
            fem_fiftybmisum += float(k)
            fem_fiftycount += 1
        if int(j) > 59 and int(j) < 70:
            fem_sixbmisum += float(k)
            fem_sixcount += 1
    if i == 'male':
        if int(j) > 17 and int(j) < 20:
            male_teenbmisum += float(k)
            male_teencount += 1
        if int(j) > 19 and int(j) < 30:
            male_twenbmisum += float(k)
            male_twencount += 1
        if int(j) > 29 and int(j) < 40:
            male_thirbmisum += float(k)
            male_thircount += 1
        if int(j) > 39 and int(j) < 50:
            male_fortbmisum += float(k)
            male_fortcount += 1
        if int(j) > 49 and int(j) < 60:
            male_fiftybmisum += float(k)
            male_fiftycount += 1
        if int(j) > 59 and int(j) < 70:
            male_sixbmisum += float(k)
            male_sixcount += 1
        

fem_teenavgbmi = fem_teenbmisum / fem_teencount
fem_twenavgbmi = fem_twenbmisum / fem_twencount
fem_thiravgbmi = fem_thirbmisum / fem_thircount
fem_fortavgbmi = fem_fortbmisum / fem_fortcount
fem_fiftyavgbmi = fem_fiftybmisum / fem_fiftycount
fem_sixavgbmi = fem_sixbmisum / fem_sixcount

male_teenavgbmi = male_teenbmisum / male_teencount
male_twenavgbmi = male_twenbmisum / male_twencount
male_thiravgbmi = male_thirbmisum / male_thircount
male_fortavgbmi = male_fortbmisum / male_fortcount
male_fiftyavgbmi = male_fiftybmisum / male_fiftycount
male_sixavgbmi = male_sixbmisum / male_sixcount
        
        

print("If you are a female in your late teens your avg bmi is: " + str(fem_teenavgbmi))
print("If you are a female in your twenties your avg bmi is: " + str(fem_twenavgbmi))
print("If you are a female in your thirties your avg bmi is: " + str(fem_thiravgbmi))
print("If you are a female in your forties your avg bmi is: " + str(fem_fortavgbmi))
print("If you are a female in your fifties your avg bmi is: " + str(fem_fiftyavgbmi))
print("If you are a female in your sixties your avg bmi is: " + str(fem_sixavgbmi))

print("If you are a male in your late teens your avg bmi is: " + str(male_teenavgbmi))
print("If you are a male in your twenties your avg bmi is: " + str(male_twenavgbmi))
print("If you are a male in your thirties your avg bmi is: " + str(male_thiravgbmi))
print("If you are a male in your forties your avg bmi is: " + str(male_fortavgbmi))
print("If you are a male in your fifties your avg bmi is: " + str(male_fiftyavgbmi))
print("If you are a male in your sixties your avg bmi is: " + str(male_sixavgbmi))


# In[12]:


#ESTO SIRVE PARA SACAR EL PROMEDIO BMI POR REGION

bmibyregion = list(zip(regions, bmis))

sum_ne = 0
sum_nw = 0
sum_se = 0
sum_sw = 0

count_ne = 0
count_nw = 0
count_se = 0
count_sw = 0

for i, j in bmibyregion:
    if i == 'northeast':
        sum_ne += float(j)
        count_ne += 1
    if i == 'northwest':
        sum_nw += float(j)
        count_nw += 1
    if i == 'southeast':
        sum_se += float(j)
        count_se += 1
    if i == 'southwest':
        sum_sw += float(j)
        count_sw += 1

avgbmi_ne = sum_ne / count_ne
avgbmi_nw = sum_nw / count_nw
avgbmi_se = sum_se / count_se
avgbmi_sw = sum_sw / count_sw

print("The average BMI for the northeast regions is: " + str(avgbmi_ne))
print("The average BMI for the northwest regions is: " + str(avgbmi_nw))
print("The average BMI for the southeast regions is: " + str(avgbmi_se))
print("The average BMI for the southwest regions is: " + str(avgbmi_sw))



# In[13]:


#ESTO ES PARA SACAR EL COSTO PROMEDIO DE INSURANCE POR RANGO DE EDAD

ageandcost = list(zip(ages, insurance_charges))

sumcost_teens = 0
sumcost_twenties = 0
sumcost_thirties = 0
sumcost_forties = 0
sumcost_fifties = 0
sumcost_sixties = 0

for i, j in ageandcost:
    if int(i) > 17 and int(i) < 20:
        sumcost_teens += float(j)
    if int(i) > 19 and int(i) < 30:
        sumcost_twenties += float(j)
    if int(i) > 29 and int(i) < 40:
        sumcost_thirties += float(j)
    if int(i) > 39 and int(i) < 50:
        sumcost_forties += float(j)
    if int(i) > 49 and int(i) < 60:
        sumcost_fifties += float(j)
    if int(i) > 59 and int(i) < 70:
        sumcost_sixties += float(j)
            
avgcost_teens = sumcost_teens / (fem_teencount + male_teencount)
avgcost_twenties = sumcost_twenties / (fem_twencount + male_twencount)
avgcost_thirties = sumcost_thirties / (fem_thircount + male_thircount)
avgcost_forties = sumcost_forties / (fem_fortcount + male_fortcount)
avgcost_fifties = sumcost_fifties / (fem_fiftycount + male_fiftycount)
avgcost_sixties = sumcost_sixties / (fem_sixcount + male_sixcount)
            
print("The average cost for someone in their teens is: " + str(avgcost_teens))
print("The average cost for someone in their twenties is: " + str(avgcost_twenties))
print("The average cost for someone in their thirties is: " + str(avgcost_thirties))
print("The average cost for someone in their forties is: " + str(avgcost_forties))
print("The average cost for someone in their fifties is: " + str(avgcost_fifties))
print("The average cost for someone in their sixties is: " + str(avgcost_sixties))


# In[ ]:




