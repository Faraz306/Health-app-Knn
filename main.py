import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import platform  # ✅ New built-in tool to check the operating system

# ✅ Smart Import: Only load winsound if running on Windows!
if platform.system() == "Windows":
    import winsound
else:
    winsound = None


st.title("YF CHECK HEART DETAILS 💝")
disease = st.selectbox("select option", ['chest pain', 'fbs', 'restecg', 'slope', 'ca', 'thal'])
if disease == "chest pain":
    df = pd.read_csv('heart.csv')
    agei = st.slider("Select age", min_value=0, max_value=100, value=100, key='1')
    which_type = st.selectbox('type of cpt', ['Typical Angina'
        , 'Atypical Angina'
        , 'Non-anginal Pain'
        , 'Asymptomatic'])
    if which_type == "Typical Angina":
        x = df[['age']]
        y = df['target']

        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(x, y)

        # --- THE FIX ---
        # Predict on the full dataset 'x' to get matching dimensions for the matrix
        y_pred = knn.predict(x)

        # Calculate overall metrics safely
        tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()

        # --- OPTIONAL: USE YOUR SLIDER VALUE ---
        # If you want to use the slider value 'agei' to see its direct risk probability:
        slider_prob = knn.predict_proba([[agei]])
        risk_percentage = slider_prob[0][1] * 100

        st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
        # Sound notification logic based on risk score
        if risk_percentage >= 50.0:
            # ✅ Safe wrapper added for high-risk beep
            if winsound:
                winsound.Beep(1200, 150)
                winsound.Beep(300, 150)
                winsound.Beep(1200, 150)
                winsound.Beep(300, 300)
            st.error("🚨 High Risk Alert Tone Played!")
        else:
            if winsound:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 250)
            st.success("🎵 Low Risk Tone Played!")

    elif which_type == "Atypical Angina":
        # 1. Filter your data
        x = df[['age']]
        y = df['target']

        # 2. Find out exactly how many patient records are available
        available_samples = len(x)

        # 3. Dynamic Neighbor Fix: Choose 5, or drop down to the max available rows
        chosen_neighbors = min(5, available_samples)

        # 4. Safely initialize your KNN model with the adjusted neighbor count
        knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)
        knn.fit(x, y)

        # 5. Run your prediction safely without any crashing!
        y_pred = knn.predict(x)
        tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()

        # 1. Get the raw decimal probabilities array [[prob_of_0, prob_of_1]]
        slider_prob = knn.predict_proba([[agei]])

        # 2. Extract index [0][1] (Class 1 / Heart Disease) and multiply by 100
        risk_percentage = slider_prob[0][1] * 100

        # 3. Print your exact formatted string to the screen!
        st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
        if risk_percentage >= 50.0:
            # ✅ Safe wrapper added for high-risk beep
            if winsound:
                winsound.Beep(1200, 150)
                winsound.Beep(300, 150)
                winsound.Beep(1200, 150)
                winsound.Beep(300, 300)
            st.error("🚨 High Risk Alert Tone Played!")
        else:
            if winsound:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 250)
            st.success("🎵 Low Risk Tone Played!")

    elif which_type == "Non-anginal Pain":
        x = df[['age']]
        y = df['target']

        available_samples = len(x)
        chosen_neighbors = min(5, available_samples)
        knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)
        knn.fit(x, y)
        y_pred = knn.predict(x)
        tn, fp, fn, tp = confusion_matrix(y, y_pred).ravel()

        slider_prob = knn.predict_proba([[agei]])
        risk_percentage = slider_prob[0][1] * 100
        st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
        if risk_percentage >= 50.0:
            # ✅ Safe wrapper added for high-risk beep
            if winsound:
                winsound.Beep(1200, 150)
                winsound.Beep(300, 150)
                winsound.Beep(1200, 150)
                winsound.Beep(300, 300)
            st.error("🚨 High Risk Alert Tone Played!")
        else:
            if winsound:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 250)
            st.success("🎵 Low Risk Tone Played!")
    elif which_type == "Asymptomatic":
        x = df[['age']]
        y = df['target']

        available_samples = len(x)
        chosen_neighbors = min(5, available_samples)

        knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

        knn.fit(x, y)

        prediction = knn.predict(x)

        tn, tp, fn, fp = confusion_matrix(y, prediction).ravel()


        slider_prob = knn.predict_proba([[agei]])

        risk_percentage = slider_prob[0][1] * 100

        st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
        if risk_percentage >= 50.0:
            # ✅ Safe wrapper added for high-risk beep
            if winsound:
                winsound.Beep(1200, 150)
                winsound.Beep(300, 150)
                winsound.Beep(1200, 150)
                winsound.Beep(300, 300)
            st.error("🚨 High Risk Alert Tone Played!")
        else:
            if winsound:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 250)
            st.success("🎵 Low Risk Tone Played!")
elif disease == 'fbs':
    df = pd.read_csv('heart.csv')
    agei = st.slider('Age', min_value=0, max_value=100, value=0, key='2')
    what_type = st.selectbox("Select", ['High Blood pressure', 'Low Blood pressure'])
    if what_type == 'High Blood pressure':
        x = df[['age', 'fbs']]
        y = df['target']

        available_samples = len(x)
        chosen_neighbors = min(5, available_samples)

        knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

        knn.fit(x, y)

        # Predict on FULL dataset for confusion matrix
        prediction = knn.predict(x)

        cm = confusion_matrix(y, prediction)

        tn, fp, fn, tp = cm.ravel()

        # Predict for ONE user
        slider_prob = knn.predict_proba([[agei, 1]])

        risk_percentage = slider_prob[0][1] * 100

        st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
        if risk_percentage >= 50.0:
            # ✅ Safe wrapper added for high-risk beep
            if winsound:
                winsound.Beep(1200, 150)
                winsound.Beep(300, 150)
                winsound.Beep(1200, 150)
                winsound.Beep(300, 300)
            st.error("🚨 High Risk Alert Tone Played!")
        else:
            if winsound:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 250)
            st.success("🎵 Low Risk Tone Played!")
    elif what_type == 'Low Blood pressure':
        x = df[['age', 'fbs']]
        y = df['target']

        available_samples = len(x)
        chosen_neighbors = min(5, available_samples)

        knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

        knn.fit(x, y)
        prediction = knn.predict(x)

        cm = confusion_matrix(y, prediction)

        tn, fp, fn, tp = cm.ravel()

        slider_prob = knn.predict_proba([[agei, 0]])

        risk_percentage = slider_prob[0][1] * 100

        st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
        if risk_percentage >= 50.0:
            # ✅ Safe wrapper added for high-risk beep
            if winsound:
                winsound.Beep(1200, 150)
                winsound.Beep(300, 150)
                winsound.Beep(1200, 150)
                winsound.Beep(300, 300)
            st.error("🚨 High Risk Alert Tone Played!")
        else:
            if winsound:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 250)
            st.success("🎵 Low Risk Tone Played!")
elif disease == 'restecg':
    df = pd.read_csv('heart.csv')
    agei = st.slider('Age', min_value=0, max_value=100, value=0, key='3')
    what_type = st.selectbox("Select", ['Normal', 'ST-T wave abnormality', 'Left Ventricular Hypertrophy'])
    if what_type == 'Normal':
        x = df[['age', 'restecg']]
        y = df['target']

        available_samples = len(x)

        chosen_neighbors = min(5, available_samples)

        knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

        knn.fit(x, y)

        prediction = knn.predict(x)

        cm = confusion_matrix(y, prediction)

        tn, fp, fn, tp = cm.ravel()

        slider_prob = knn.predict_proba([[agei, 0]])

        risk_percentage = slider_prob[0][1] * 100

        st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
        if risk_percentage >= 50.0:
            # ✅ Safe wrapper added for high-risk beep
            if winsound:
                winsound.Beep(1200, 150)
                winsound.Beep(300, 150)
                winsound.Beep(1200, 150)
                winsound.Beep(300, 300)
            st.error("🚨 High Risk Alert Tone Played!")
        else:
            if winsound:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 250)
            st.success("🎵 Low Risk Tone Played!")
    elif what_type == 'ST-T wave abnormality':
            x = df[['age', 'restecg']]
            y = df['target']

            available_samples = len(x)

            chosen_neighbors = min(5, available_samples)

            knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

            knn.fit(x, y)

            prediction = knn.predict(x)

            cm = confusion_matrix(y, prediction)

            tn, fp, fn, tp = cm.ravel()

            slider_prob = knn.predict_proba([[agei, 1]])

            risk_percentage = slider_prob[0][1] * 100

            st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
            if risk_percentage >= 50.0:
                # ✅ Safe wrapper added for high-risk beep
                if winsound:
                    winsound.Beep(1200, 150)
                    winsound.Beep(300, 150)
                    winsound.Beep(1200, 150)
                    winsound.Beep(300, 300)
                st.error("🚨 High Risk Alert Tone Played!")
            else:
                if winsound:
                    winsound.Beep(523, 150)
                    winsound.Beep(659, 150)
                    winsound.Beep(784, 250)
                st.success("🎵 Low Risk Tone Played!")
    elif what_type == 'Left Ventricular Hypertrophy':
        # ✅ 1. Make sure x is extracted from your df (Double brackets keep it a DataFrame)
        x = df[['age', 'restecg']]  # Replace 'fbs' with whatever column you are analyzing here
        y = df['target']

        # ✅ 2. Now this will run perfectly without throwing an AttributeError!
        x = x.apply(pd.to_numeric, errors='coerce')
        y = pd.to_numeric(y, errors='coerce')

        # Drop any rows that couldn't be converted (just in case there are text errors)
        x = x.dropna()
        y = y[x.index]

        available_samples = len(x)
        chosen_neighbors = min(5, available_samples)

        knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

        knn.fit(x, y)

        prediction = knn.predict(x)

        cm = confusion_matrix(y, prediction)

        tn, fp, fn, tp = cm.ravel()

        slider_prob = knn.predict_proba([[agei, 2]])

        risk_percentage = slider_prob[0][1] * 100

        st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
        if risk_percentage >= 50.0:
            # ✅ Safe wrapper added for high-risk beep
            if winsound:
                winsound.Beep(1200, 150)
                winsound.Beep(300, 150)
                winsound.Beep(1200, 150)
                winsound.Beep(300, 300)
            st.error("🚨 High Risk Alert Tone Played!")
        else:
            if winsound:
                winsound.Beep(523, 150)
                winsound.Beep(659, 150)
                winsound.Beep(784, 250)
            st.success("🎵 Low Risk Tone Played!")
elif disease == 'ca':
     df = pd.read_csv('heart.csv')
     agei = st.slider('Age', min_value=0, max_value=100, value=0, key='4')
     what_type = st.selectbox("Select", ['0 Vessels Clear 💀', '1 vessel clear ⚠', '2 vessels clear 👍', '3 vessels clear 💝'])
     if what_type == '0 Vessels Clear 💀':
         x = df[['age', 'ca']]  # (Change 'slope' to match whichever branch you are in)
         y = df['target']

         # ✅ 2. Now line 348 will execute flawlessly!
         x = x.apply(pd.to_numeric, errors='coerce')
         y = pd.to_numeric(y, errors='coerce')

         available_samples = len(x)
         chosen_neighbors = min(5, available_samples)

         knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

         knn.fit(x, y)

         prediction = knn.predict(x)

         cm = confusion_matrix(y, prediction)

         tn, fp, fn, tp = cm.ravel()

         slider_prob = knn.predict_proba([[agei, 0]])

         risk_percentage = slider_prob[0][1] * 100

         st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
         if risk_percentage >= 50.0:
             # ✅ Safe wrapper added for high-risk beep
             if winsound:
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 150)
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 300)
             st.error("🚨 High Risk Alert Tone Played!")
         else:
             if winsound:
                 winsound.Beep(523, 150)
                 winsound.Beep(659, 150)
                 winsound.Beep(784, 250)
             st.success("🎵 Low Risk Tone Played!")
     if what_type == '1 vessel clear ⚠':
         x = df[['age', 'ca']]  # (Change 'slope' to match whichever branch you are in)
         y = df['target']

         # ✅ 2. Now line 348 will execute flawlessly!
         x = x.apply(pd.to_numeric, errors='coerce')
         y = pd.to_numeric(y, errors='coerce')

         available_samples = len(x)
         chosen_neighbors = min(5, available_samples)

         knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

         knn.fit(x, y)

         prediction = knn.predict(x)

         cm = confusion_matrix(y, prediction)

         tn, fp, fn, tp = cm.ravel()

         slider_prob = knn.predict_proba([[agei, 1]])

         risk_percentage = slider_prob[0][1] * 100

         st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
         if risk_percentage >= 50.0:
             # ✅ Safe wrapper added for high-risk beep
             if winsound:
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 150)
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 300)
             st.error("🚨 High Risk Alert Tone Played!")
         else:
             if winsound:
                 winsound.Beep(523, 150)
                 winsound.Beep(659, 150)
                 winsound.Beep(784, 250)
             st.success("🎵 Low Risk Tone Played!")
     if what_type == '2 vessels clear 👍':
         x = df[['age', 'ca']]  # (Change 'slope' to match whichever branch you are in)
         y = df['target']

         # ✅ 2. Now line 348 will execute flawlessly!
         x = x.apply(pd.to_numeric, errors='coerce')
         y = pd.to_numeric(y, errors='coerce')

         available_samples = len(x)
         chosen_neighbors = min(5, available_samples)

         knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

         knn.fit(x, y)

         prediction = knn.predict(x)

         cm = confusion_matrix(y, prediction)

         tn, fp, fn, tp = cm.ravel()

         slider_prob = knn.predict_proba([[agei, 2]])

         risk_percentage = slider_prob[0][1] * 100

         st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
         if risk_percentage >= 50.0:
             # ✅ Safe wrapper added for high-risk beep
             if winsound:
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 150)
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 300)
             st.error("🚨 High Risk Alert Tone Played!")
         else:
             if winsound:
                 winsound.Beep(523, 150)
                 winsound.Beep(659, 150)
                 winsound.Beep(784, 250)
             st.success("🎵 Low Risk Tone Played!")
     if what_type == '3 vessels clear 💝':
         x = df[['age', 'ca']]  # (Change 'slope' to match whichever branch you are in)
         y = df['target']

         # ✅ 2. Now line 348 will execute flawlessly!
         x = x.apply(pd.to_numeric, errors='coerce')
         y = pd.to_numeric(y, errors='coerce')

         available_samples = len(x)
         chosen_neighbors = min(5, available_samples)

         knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

         knn.fit(x, y)

         prediction = knn.predict(x)

         cm = confusion_matrix(y, prediction)

         tn, fp, fn, tp = cm.ravel()

         slider_prob = knn.predict_proba([[agei, 3]])

         risk_percentage = slider_prob[0][1] * 100

         st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
         if risk_percentage >= 50.0:
             # ✅ Safe wrapper added for high-risk beep
             if winsound:
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 150)
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 300)
             st.error("🚨 High Risk Alert Tone Played!")
         else:
             if winsound:
                 winsound.Beep(523, 150)
                 winsound.Beep(659, 150)
                 winsound.Beep(784, 250)
             st.success("🎵 Low Risk Tone Played!")

elif disease == 'thal':
     df = pd.read_csv('heart.csv')
     agei = st.slider('Age', min_value=0, max_value=100, value=0, key='4')
     what_type = st.selectbox("Select", ['normal flow', 'fixed defect', 'reversible defect'])
     if what_type == 'normal flow':
         x = df[['age', 'thal']]  # (Change 'slope' to match whichever branch you are in)
         y = df['target']

         # ✅ 2. Now line 348 will execute flawlessly!
         x = x.apply(pd.to_numeric, errors='coerce')
         y = pd.to_numeric(y, errors='coerce')

         available_samples = len(x)
         chosen_neighbors = min(5, available_samples)

         knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

         knn.fit(x, y)

         prediction = knn.predict(x)

         cm = confusion_matrix(y, prediction)

         tn, fp, fn, tp = cm.ravel()

         slider_prob = knn.predict_proba([[agei, 0]])

         risk_percentage = slider_prob[0][1] * 100

         st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
         if risk_percentage >= 50.0:
             # ✅ Safe wrapper added for high-risk beep
             if winsound:
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 150)
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 300)
             st.error("🚨 High Risk Alert Tone Played!")
         else:
             if winsound:
                 winsound.Beep(523, 150)
                 winsound.Beep(659, 150)
                 winsound.Beep(784, 250)
             st.success("🎵 Low Risk Tone Played!")
     if what_type == 'fixed defect':
         x = df[['age', 'thal']]  # (Change 'slope' to match whichever branch you are in)
         y = df['target']

         # ✅ 2. Now line 348 will execute flawlessly!
         x = x.apply(pd.to_numeric, errors='coerce')
         y = pd.to_numeric(y, errors='coerce')

         available_samples = len(x)
         chosen_neighbors = min(5, available_samples)

         knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

         knn.fit(x, y)

         prediction = knn.predict(x)

         cm = confusion_matrix(y, prediction)

         tn, fp, fn, tp = cm.ravel()

         slider_prob = knn.predict_proba([[agei, 1]])

         risk_percentage = slider_prob[0][1] * 100

         st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
         if risk_percentage >= 50.0:
             # ✅ Safe wrapper added for high-risk beep
             if winsound:
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 150)
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 300)
             st.error("🚨 High Risk Alert Tone Played!")
         else:
             if winsound:
                 winsound.Beep(523, 150)
                 winsound.Beep(659, 150)
                 winsound.Beep(784, 250)
             st.success("🎵 Low Risk Tone Played!")
     if what_type == 'reversible defect':
         x = df[['age', 'thal']]  # (Change 'slope' to match whichever branch you are in)
         y = df['target']

         # ✅ 2. Now line 348 will execute flawlessly!
         x = x.apply(pd.to_numeric, errors='coerce')
         y = pd.to_numeric(y, errors='coerce')

         available_samples = len(x)
         chosen_neighbors = min(5, available_samples)

         knn = KNeighborsClassifier(n_neighbors=chosen_neighbors)

         knn.fit(x, y)

         prediction = knn.predict(x)

         cm = confusion_matrix(y, prediction)

         tn, fp, fn, tp = cm.ravel()

         slider_prob = knn.predict_proba([[agei, 2]])

         risk_percentage = slider_prob[0][1] * 100

         st.info(f"💡 Risk percentage for a patient aged {agei}: {risk_percentage:.1f}%")
         if risk_percentage >= 50.0:
             # ✅ Safe wrapper added for high-risk beep
             if winsound:
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 150)
                 winsound.Beep(1200, 150)
                 winsound.Beep(300, 300)
             st.error("🚨 High Risk Alert Tone Played!")
         else:
             if winsound:
                 winsound.Beep(523, 150)
                 winsound.Beep(659, 150)
                 winsound.Beep(784, 250)
             st.success("🎵 Low Risk Tone Played!")