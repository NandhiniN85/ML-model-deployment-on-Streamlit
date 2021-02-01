 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('model.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(mpg,cyl,disp,hp,wt,acc,yr,origin):  
 
    # Making predictions 
    prediction = classifier.predict( 
        [[mpg,cyl,disp,hp,wt,acc,yr,origin]])
     
    if prediction == 0:
        pred = 'The input is not an anomaly'
    else:
        pred = 'The input is an anomaly'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Anomaly Detection ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    mpg = st.number_input("mpg") 
    cyl = st.number_input("cyl") 
    disp = st.number_input("disp") 
    hp = st.number_input("hp")
    wt = st.number_input("wt")
    acc = st.number_input("acc")
    yr = st.number_input("yr")
    origin = st.number_input("origin")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(mpg, cyl, disp, hp, wt, acc, yr, origin) 
        st.success('Outlier Status : {}'.format(result))
     
if __name__=='__main__': 
    main()
