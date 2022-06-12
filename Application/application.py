import tkinter as GUI_Framework
#GUI related works


import pandas as pd
import numpy as np
#used for data_manipulation

import joblib
#Loading pretrained ML Models into GUI


from sklearn.preprocessing import LabelEncoder
#changing categorical data to numerical data for feeding to GUI
import warnings
warnings.filterwarnings('ignore',category=UserWarning)

def user_manual(application_Frame):
    file=open('about.txt','a')
    file=open('about.txt','r')
    li=file.readlines()
    if not li:
        GUI_Framework.Label(application_Frame,text="No File Exists").pack()
        file.close()
        GUI_Framework.Label(application_Frame,text='').pack()
        back=GUI_Framework.Button(application_Frame,text="GO BACK",command=lambda:greeting_screen(application_Frame))
        back.pack()
    else:
        scrollbar = GUI_Framework.Scrollbar(application_Frame)
        scrollbar.pack( side = 'right', fill = 'y' )
        mylist=GUI_Framework.Listbox(application_Frame, height=20,width=100,yscrollcommand=scrollbar.set)
            
        for i in range(0,len(li)):
            mylist.insert(GUI_Framework.END,li[i])
        mylist.pack()
        scrollbar.config(command=mylist.yview)
        file.close()


def show_user_entries_and_proceed_to_predict_kidney_disease(application_Frame,age,bp,albumin,bgr,blood_urea,serum_creatinine,haemoglobin,packed_cell_volume,rbc_count,hypertension,diabetes_mellitus,appetite,anaemia):
    application_Frame.destroy()
    
    application_Frame=GUI_Framework.Frame(application_main_window)
    application_Frame.pack()

    main_title=GUI_Framework.Label(application_Frame,text="Multiple Disease Prediction System",font=('Times New Roman',20,'bold'))
    main_title.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()

    sub_title=GUI_Framework.Label(application_Frame,text="Chronic Kidney Disease Prediction",font=('Times New Roman',18,'bold','underline'))
    sub_title.pack()    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()

    sub_title=GUI_Framework.Label(application_Frame,text="Confirm Entries",font=('Times New Roman',18,'bold'))
    sub_title.pack()    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    entries=GUI_Framework.Listbox(application_Frame,height=13,width=45)
    entries.insert(GUI_Framework.END,'Age :{}'.format(age))
    entries.insert(GUI_Framework.END,'Blood Pressure :{}'.format(bp))
    entries.insert(GUI_Framework.END,'Albumin :{}'.format(albumin))
    entries.insert(GUI_Framework.END,'Blood Glucose Random :{}'.format(bgr))
    entries.insert(GUI_Framework.END,'Blood Urea :{}'.format(blood_urea))
    entries.insert(GUI_Framework.END,'Serum Creatinine :{}'.format(serum_creatinine))
    entries.insert(GUI_Framework.END,'Haemoglobin :{}'.format(haemoglobin))
    entries.insert(GUI_Framework.END,'Packed Cell Volume :{}'.format(packed_cell_volume))
    entries.insert(GUI_Framework.END,'Red Blood Cell Count :{}'.format(rbc_count))
    entries.insert(GUI_Framework.END,'Hypertension :{}'.format(hypertension))
    entries.insert(GUI_Framework.END,'Diabetes Mellitus :{}'.format(diabetes_mellitus))
    entries.insert(GUI_Framework.END,'Appetite :{}'.format(appetite))
    entries.insert(GUI_Framework.END,'Anaemia :{}'.format(anaemia))    
    entries.pack()    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()    

    button_to_back=GUI_Framework.Button(application_Frame,text="Go Back",command=lambda:chronic_kidney_disease_prediction(application_Frame),font=('Times New Roman',10,'bold'),borderwidth=0)
    button_to_back.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    def entries_confirmed_predict_kidney_disease(application_Frame):
        values=[[]]
        values[0].append(age)
        values[0].append(bp)
        values[0].append(albumin)
        values[0].append(bgr)
        values[0].append(blood_urea)
        values[0].append(serum_creatinine)
        values[0].append(haemoglobin)
        values[0].append(packed_cell_volume)
        values[0].append(rbc_count)
        values[0].append(hypertension)
        values[0].append(diabetes_mellitus)
        values[0].append(appetite)
        values[0].append(anaemia)
        

        user_data=pd.DataFrame(values,columns=['age', 'blood_pressure', 'albumin', 'blood_glucose_random','blood_urea', 'serum_creatinine', 'haemoglobin', 'packed_cell_volume','red_blood_cell_count', 'hypertension', 'diabetes_mellitus', 'appetite','aanemia'])
        
        user_data['blood_urea'] =np.log1p(user_data['blood_urea'])
        user_data['serum_creatinine'] =np.log1p(user_data['serum_creatinine'])
        
        encode = LabelEncoder()
        user_data['hypertension']=encode.fit_transform(user_data['hypertension'])
        user_data['diabetes_mellitus']=encode.fit_transform(user_data['diabetes_mellitus'])
        user_data['appetite']=encode.fit_transform(user_data['appetite'])
        user_data['aanemia']=encode.fit_transform(user_data['aanemia'])
        
        improved_random_forest_pretrained_model=joblib.load("Improved_2_RandomForest-Model-Kidney_Disease.pkl")
        
        result=improved_random_forest_pretrained_model.predict(user_data)
        
        for i in result:
            output_value=i
        if output_value==0:
            result_by_model.config(text="Chronic Kidney Disease Detected")
        else:
            result_by_model.config(text="Chronic Kidney Disease Not Detected")

        
        
        
    button_to_confirm=GUI_Framework.Button(application_Frame,text="Confirm",command=lambda:entries_confirmed_predict_kidney_disease(application_Frame),font=('Times New Roman',11,'bold'),borderwidth=0)
    button_to_confirm.pack()
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack() 
    button_to_quit=GUI_Framework.Button(application_Frame,text='Quit',command=lambda:quit_Application(application_main_window),font=('Times New Roman',10,'bold'),borderwidth=0)
    button_to_quit.pack()
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack() 
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack() 
    result_by_model=GUI_Framework.Label(application_Frame,text='',font=('Times New Roman',15,'bold','underline'))
    result_by_model.pack()
    
    
def chronic_kidney_disease_prediction(application_Frame):
    application_Frame.destroy()
    
    application_Frame=GUI_Framework.Frame(application_main_window)
    application_Frame.pack()
    
    main_title=GUI_Framework.Label(application_Frame,text="Multiple Disease Prediction System",font=('Times New Roman',20,'bold'))
    main_title.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()

    sub_title=GUI_Framework.Label(application_Frame,text="Chronic Kidney Disease Prediction",font=('Times New Roman',18,'bold','underline'))
    sub_title.pack()
    
    
    label_for_age=GUI_Framework.Label(application_Frame,text='Age')
    label_for_age.pack()
    
    text_for_age=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_age.pack()
    
    
    label_for_bp=GUI_Framework.Label(application_Frame,text='Blood Pressure')
    label_for_bp.pack()
    
    text_for_bp=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_bp.pack()
    
    label_for_albumin=GUI_Framework.Label(application_Frame,text='Albumin')
    label_for_albumin.pack()
    
    text_for_albumin=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_albumin.pack()
    
    
    label_for_bgr=GUI_Framework.Label(application_Frame,text='Blood Glucose Random')
    label_for_bgr.pack()
    
    text_for_bgr=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_bgr.pack()
    
    label_for_blood_urea=GUI_Framework.Label(application_Frame,text='Blood Urea')
    label_for_blood_urea.pack()
    
    text_for_blood_urea=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_blood_urea.pack()
    
    label_for_serum_creatinine=GUI_Framework.Label(application_Frame,text='Serum Creatinine')
    label_for_serum_creatinine.pack()
    
    text_for_serum_creatinine=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_serum_creatinine.pack()
    
    label_for_haemoglobin=GUI_Framework.Label(application_Frame,text='Haemoglobin')
    label_for_haemoglobin.pack()
    
    text_for_haemoglobin=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_haemoglobin.pack()
    
    label_for_packed_cell_volume=GUI_Framework.Label(application_Frame,text='Packed Cell Volume')
    label_for_packed_cell_volume.pack()
    
    text_for_packed_cell_volume=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_packed_cell_volume.pack()
    
    label_for_rbc_count=GUI_Framework.Label(application_Frame,text='Red Blood Cell Count')
    label_for_rbc_count.pack()
    
    text_for_rbc_count=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_rbc_count.pack()
    
    label_for_hypertension=GUI_Framework.Label(application_Frame,text='Hypertension')
    label_for_hypertension.pack()
    
    text_for_hypertension=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_hypertension.pack()
    
    label_for_diabetes_mellitus=GUI_Framework.Label(application_Frame,text='Diabetes Mellitus')
    label_for_diabetes_mellitus.pack()
    
    text_for_diabetes_mellitus=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_diabetes_mellitus.pack()
    
    label_for_appetite=GUI_Framework.Label(application_Frame,text='Appetite')
    label_for_appetite.pack()
    
    text_for_appetite=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_appetite.pack()
    
    label_for_anaemia=GUI_Framework.Label(application_Frame,text='Anaemia')
    label_for_anaemia.pack()
    
    text_for_anaemia=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_anaemia.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    button_to_back=GUI_Framework.Button(application_Frame,text="Go Back",command=lambda:get_prediction_of_disease(application_Frame),font=('Times New Roman',10,'bold'),borderwidth=0)
    button_to_back.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    def check_entries_kidney(application_Frame):
        age=text_for_age.get('1.0','end-1c')
        bp=text_for_bp.get('1.0','end-1c')
        albumin=text_for_albumin.get('1.0','end-1c')
        bgr=text_for_bgr.get('1.0','end-1c')
        blood_urea=text_for_blood_urea.get('1.0','end-1c')
        serum_creatinine=text_for_serum_creatinine.get('1.0','end-1c')
        haemoglobin=text_for_haemoglobin.get('1.0','end-1c')
        packed_cell_volume=text_for_packed_cell_volume.get('1.0','end-1c')
        rbc_count=text_for_rbc_count.get('1.0','end-1c')
        hypertension=text_for_hypertension.get('1.0','end-1c')
        diabetes_mellitus=text_for_diabetes_mellitus.get('1.0','end-1c')
        appetite=text_for_appetite.get('1.0','end-1c')
        anaemia=text_for_anaemia.get('1.0','end-1c')
        
        if (not age) or (not bp) or (not albumin) or (not bgr) or (not blood_urea) or (not serum_creatinine) or (not haemoglobin) or (not packed_cell_volume) or (not rbc_count) or (not hypertension) or (not diabetes_mellitus) or (not appetite) or (not anaemia):
            message_to_user.config(text='Please Fill All Entries')
            
        try:
            age=float(age)
            bp=float(bp)
            albumin=float(albumin)
            bgr=float(bgr)
            blood_urea=float(blood_urea)
            serum_creatinine=float(serum_creatinine)
            haemoglobin=float(haemoglobin)
            packed_cell_volume=float(packed_cell_volume)
            rbc_count=float(rbc_count)
        except ValueError:
            message_to_user.config(text="Please Fill Numeric Values In All Entries Except the Last 4 Entries")
        else:
            hypertension=hypertension.strip()
            diabetes_mellitus=diabetes_mellitus.strip()
            appetite=appetite.strip()
            anaemia=anaemia.strip()
            
            hypertension=hypertension.lower()
            diabetes_mellitus=diabetes_mellitus.lower()
            appetite=appetite.lower()
            anaemia=anaemia.lower()
            ans=['yes','no']
            app=['good','poor']
            if hypertension in ans:
                if diabetes_mellitus in ans:
                    if appetite in app:
                        if anaemia in ans:
                            show_user_entries_and_proceed_to_predict_kidney_disease(application_Frame,age,bp,albumin,bgr,blood_urea,serum_creatinine,haemoglobin,packed_cell_volume,rbc_count,hypertension,diabetes_mellitus,appetite,anaemia)
                        else:
                            message_to_user.config(text='Please Enter Correct Values ')
                    else:
                        message_to_user.config(text='Please Enter Correct Values ')
                else:
                    message_to_user.config(text='Please Enter Correct Values ')
            else:
                message_to_user.config(text='Please Enter Correct Values ')
            
             
    verify_button=GUI_Framework.Button(application_Frame,text='Verify',command=lambda:check_entries_kidney(application_Frame),font=('Times New Roman',14,'bold','underline'),borderwidth=0)
    verify_button.pack()
    
    message_to_user=GUI_Framework.Label(application_Frame,text='',font=('Times New Roman',11,'bold','underline'))
    message_to_user.pack()
    
    
def show_user_entries_and_proceed_to_predict_liver_disease(application_Frame,age,gender,total_bilirubin,direct_bilirubin,alkaline_phosphotase,alanine_aminotransferace,aspartate_aminotransferace,total_proteins,albumin):
    application_Frame.destroy()
    
    application_Frame=GUI_Framework.Frame(application_main_window)
    application_Frame.pack()

    main_title=GUI_Framework.Label(application_Frame,text="Multiple Disease Prediction System",font=('Times New Roman',20,'bold'))
    main_title.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()

    sub_title=GUI_Framework.Label(application_Frame,text="Liver Disease Prediction",font=('Times New Roman',18,'bold','underline'))
    sub_title.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()

    sub_title=GUI_Framework.Label(application_Frame,text="Confirm Entries",font=('Times New Roman',18,'bold'))
    sub_title.pack()    
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    entries=GUI_Framework.Listbox(application_Frame,height=13,width=45)
    entries.insert(GUI_Framework.END,'Age :{}'.format(age))
    entries.insert(GUI_Framework.END,'Gender :{}'.format(gender))
    entries.insert(GUI_Framework.END,'Total Bilirubin :{}'.format(total_bilirubin))
    entries.insert(GUI_Framework.END,'Direct Bilirubin :{}'.format(direct_bilirubin))
    entries.insert(GUI_Framework.END,'Alkaline Phosphate :{}'.format(alkaline_phosphotase))
    entries.insert(GUI_Framework.END,'Alanine Aminotransferase :{}'.format(alanine_aminotransferace))
    entries.insert(GUI_Framework.END,'Aspartate Aminotransferase :{}'.format(aspartate_aminotransferace))
    entries.insert(GUI_Framework.END,'Total Proteins :{}'.format(total_proteins))
    entries.insert(GUI_Framework.END,'Albumin :{}'.format(albumin))
    entries.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()    

    button_to_back=GUI_Framework.Button(application_Frame,text="Go Back",command=lambda:liver_disease_prediction(application_Frame),font=('Times New Roman',10,'bold'),borderwidth=0)
    button_to_back.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    def entries_confirmed_predict_liver_disease(application_Frame):
        values=[[]]
        values[0].append(age)
        values[0].append(gender)
        values[0].append(total_bilirubin)
        values[0].append(direct_bilirubin)
        values[0].append(alkaline_phosphotase)
        values[0].append(alanine_aminotransferace)
        values[0].append(aspartate_aminotransferace)
        values[0].append(total_proteins)
        values[0].append(albumin)
        

        user_data=pd.DataFrame(values,columns=['Age','Gender','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin'])

        enc = LabelEncoder()
        user_data['Gender'] = enc.fit_transform(user_data['Gender'].astype('str'))
        improved_random_forest_pretrained_model=joblib.load("Improved_2_Random_Forest_Model_Liver_disease.pkl")
        
        result=improved_random_forest_pretrained_model.predict(user_data)
        
        for i in result:
            output_value=i
        if output_value==1:
            result_by_model.config(text="Liver Disease Detected")
        else:
            result_by_model.config(text="Liver Disease Not Detected")

            
        
        
    button_to_confirm=GUI_Framework.Button(application_Frame,text="Confirm",command=lambda:entries_confirmed_predict_liver_disease(application_Frame),font=('Times New Roman',11,'bold'),borderwidth=0)
    button_to_confirm.pack()
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack() 
    button_to_quit=GUI_Framework.Button(application_Frame,text='Quit',command=lambda:quit_Application(application_main_window),font=('Times New Roman',10,'bold'),borderwidth=0)
    button_to_quit.pack()
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack() 
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack() 
    result_by_model=GUI_Framework.Label(application_Frame,text='',font=('Times New Roman',15,'bold','underline'))
    result_by_model.pack()
    
    
def liver_disease_prediction(application_Frame):
    application_Frame.destroy()
    
    application_Frame=GUI_Framework.Frame(application_main_window)
    application_Frame.pack()

    main_title=GUI_Framework.Label(application_Frame,text="Multiple Disease Prediction System",font=('Times New Roman',20,'bold'))
    main_title.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()

    sub_title=GUI_Framework.Label(application_Frame,text="Liver Disease Prediction",font=('Times New Roman',18,'bold','underline'))
    sub_title.pack()
    
    label_for_age=GUI_Framework.Label(application_Frame,text='Age')
    label_for_age.pack()
    
    text_for_age=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_age.pack()
    
    
    label_for_gender=GUI_Framework.Label(application_Frame,text='Gender')
    label_for_gender.pack()
    
    text_for_gender=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_gender.pack()
    
    label_for_total_bilirubin=GUI_Framework.Label(application_Frame,text='Total Bilirubin')
    label_for_total_bilirubin.pack()
    
    text_for_total_bilirubin=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_total_bilirubin.pack()
    
    
    label_for_direct_bilirubin=GUI_Framework.Label(application_Frame,text='Direct Bilirubin')
    label_for_direct_bilirubin.pack()
    
    text_for_direct_bilirubin=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_direct_bilirubin.pack()
    
    label_for_alkaline_phosphotase=GUI_Framework.Label(application_Frame,text='Alkaline Phosphotase')
    label_for_alkaline_phosphotase.pack()
    
    text_for_alkaline_phosphotase=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_alkaline_phosphotase.pack()
    
    label_for_alanine_aminotransferace=GUI_Framework.Label(application_Frame,text='Alanine Aminotransferase')
    label_for_alanine_aminotransferace.pack()
    
    text_for_alanine_aminotransferace=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_alanine_aminotransferace.pack()
    
    label_for_aspartate_aminotransferace=GUI_Framework.Label(application_Frame,text='Aspartate Aminotransferase')
    label_for_aspartate_aminotransferace.pack()
    
    text_for_aspartate_aminotransferace=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_aspartate_aminotransferace.pack()
    
    label_for_total_proteins=GUI_Framework.Label(application_Frame,text='Total Proteins')
    label_for_total_proteins.pack()
    
    text_for_total_proteins=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_total_proteins.pack()
    
    label_for_albumin=GUI_Framework.Label(application_Frame,text='Albumin')
    label_for_albumin.pack()
    
    text_for_albumin=GUI_Framework.Text(application_Frame,width=30,height=1)
    text_for_albumin.pack()

    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    button_to_back=GUI_Framework.Button(application_Frame,text="Go Back",command=lambda:get_prediction_of_disease(application_Frame),font=('Times New Roman',10,'bold'),borderwidth=0)
    button_to_back.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    def check_entries_liver(application_Frame):
        age=text_for_age.get("1.0","end-1c")
        gender=text_for_gender.get('1.0','end-1c')
        total_bilirubin=text_for_total_bilirubin.get('1.0','end-1c')
        direct_bilirubin=text_for_direct_bilirubin.get('1.0','end-1c')
        alkaline_phosphotase=text_for_alkaline_phosphotase.get('1.0','end-1c')
        alanine_aminotransferace=text_for_alanine_aminotransferace.get('1.0','end-1c')
        aspartate_aminotransferace=text_for_aspartate_aminotransferace.get('1.0','end-1c')
        total_proteins=text_for_total_proteins.get('1.0','end-1c')
        albumin=text_for_albumin.get('1.0','end-1c')
        
        if (not age) or (not gender) or (not total_bilirubin ) or (not direct_bilirubin) or (not alkaline_phosphotase) or (not alanine_aminotransferace) or (not aspartate_aminotransferace) or (not total_proteins) or (not albumin):
            message_to_user.config(text='               Please Fill All Entries                 ')
        else:
            try :
                age=int(age)
                total_bilirubin=float(total_bilirubin)
                direct_bilirubin=float(direct_bilirubin)
                alkaline_phosphotase=int(alkaline_phosphotase)
                alanine_aminotransferace=int(alanine_aminotransferace)
                aspartate_aminotransferace=int(aspartate_aminotransferace)
                total_proteins=float(total_proteins)
                albumin=float(albumin)
            except ValueError:
                message_to_user.config(text="Please Enter Numeric Value In All Sections Except Gender")
            else:
                gender=gender.strip()
                gender=gender.lower()
                if gender =="male" or gender=="female":
                    message_to_user.config(text='                                                              ')
                    show_user_entries_and_proceed_to_predict_liver_disease(application_Frame,age,gender,total_bilirubin,direct_bilirubin,alkaline_phosphotase,alanine_aminotransferace,aspartate_aminotransferace,total_proteins,albumin)
                else:
                    message_to_user.config(text='Please enter Male/Female in Gender Section')
    verify_button=GUI_Framework.Button(application_Frame,text='Verify',command=lambda:check_entries_liver(application_Frame),font=('Times New Roman',14,'bold','underline'),borderwidth=0)
    verify_button.pack()
    
    message_to_user=GUI_Framework.Label(application_Frame,text='',font=('Times New Roman',11,'bold','underline'))
    message_to_user.pack()
    
    
def get_prediction_of_disease(application_Frame):
    application_Frame.destroy()
    
    application_Frame=GUI_Framework.Frame(application_main_window)
    application_Frame.pack()

    main_title=GUI_Framework.Label(application_Frame,text="Multiple Disease Prediction System",font=('Times New Roman',20,'bold'))
    main_title.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()

    sub_title=GUI_Framework.Label(application_Frame,text="Disease Prediction",font=('Times New Roman',18,'bold','underline'))
    sub_title.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    button_to_liver_disease=GUI_Framework.Button(application_Frame,text='Liver Disease Prediction',command=lambda:liver_disease_prediction(application_Frame),font=('Times New Roman',14,'bold'))
    button_to_liver_disease.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    button_to_kidney_disease=GUI_Framework.Button(application_Frame,text='Chronic Kidney Disease Prediction',command=lambda:chronic_kidney_disease_prediction(application_Frame),font=('Times New Roman',14,'bold'))
    button_to_kidney_disease.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()    

    button_to_back=GUI_Framework.Button(application_Frame,text="Go Back",command=lambda:start_Application(application_Frame),font=('Times New Roman',14,'bold'))
    button_to_back.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    button_to_quit=GUI_Framework.Button(application_Frame,text='Quit',command=lambda:quit_Application(application_main_window),font=('Times New Roman',14,'bold'))
    button_to_quit.pack()
      

def start_Application(application_Frame):
    application_Frame.destroy()
    
    application_Frame=GUI_Framework.Frame(application_main_window)
    application_Frame.pack()


    main_title=GUI_Framework.Label(application_Frame,text="Multiple Disease Prediction System",font=('Times New Roman',20,'bold'))
    main_title.pack()

    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    sub_title=GUI_Framework.Label(application_Frame,text="Main Menu",font=('Times New Roman',18,'bold','underline'))
    sub_title.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    
    button_to_direct_predictions=GUI_Framework.Button(application_Frame,text='Instant Predictions',command=lambda:get_prediction_of_disease(application_Frame),font=('Times New Roman',14,'bold'))
    button_to_direct_predictions.pack()

    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    button_to_back=GUI_Framework.Button(application_Frame,text="Go Back",command=lambda:greeting_screen(application_Frame),font=('Times New Roman',14,'bold'))
    button_to_back.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    button_to_quit=GUI_Framework.Button(application_Frame,text='Quit',command=lambda:quit_Application(application_main_window),font=('Times New Roman',14,'bold'))
    button_to_quit.pack()

def quit_Application(application_Frame):
    application_Frame.destroy()

def greeting_screen(application_Frame):
    application_Frame.destroy()
    
    application_Frame=GUI_Framework.Frame(application_main_window)
    application_Frame.pack()
    main_title=GUI_Framework.Label(application_Frame,text="Multiple Disease Prediction System",font=('Times New Roman',20,'bold'))
    main_title.pack()
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    button_to_start=GUI_Framework.Button(application_Frame,text='Start Application',command=lambda:start_Application(application_Frame),font=('Times New Roman',14,'bold'),borderwidth=0)
    button_to_start.pack()

    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    
    button_to_guide=GUI_Framework.Button(application_Frame,text='How To Use Application',command=lambda:user_manual(application_Frame),font=('Times New Roman',14,'bold'),borderwidth=0)
    button_to_guide.pack()

    gapping=GUI_Framework.Label(application_Frame,text="")
    gapping.pack()
    button_to_quit=GUI_Framework.Button(application_Frame,text='Quit',command=lambda:quit_Application(application_main_window),font=('Times New Roman',14,'bold'),borderwidth=0)
    button_to_quit.pack()
    
    
application_main_window=GUI_Framework.Tk()
application_main_window.title('Multiple Disease Prediction System')
application_main_window.iconbitmap('application_logo.ico')
application_main_window.geometry('900x750')
application_main_window.resizable(width=True,height=True)
application_Frame=GUI_Framework.Frame(application_main_window)
application_Frame.pack()
greeting_screen(application_Frame)

application_main_window.mainloop()
