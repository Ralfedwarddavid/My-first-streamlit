import streamlit as st

st.title('Title -> GeeksforGeeks')               # Title
st.header('Header -> GeeksforGeeks')             # Header
st.subheader('Subheader -> GeeksforGeeks')       # Subheader
st.text('Text -> GeeksforGeeks')                 # Text


st.markdown('# Hi')                              # Markdown
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')

st.success('Success!')                                # success
st.info('Information!')                               # Information
st.warning('Warning!')                                # warning
st.error('Error')                                     # Error
st.exception(ZeroDivisionError('Div not possible'))

st.subheader('Help')
st.help(ZeroDivisionError)                             # Help

st.subheader('Write')
st.write("range(1,10)")                                # Write
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.subheader('Code')
st.code('x = 10\n'                                     # Code
         'for i in range(x):\n'
         '\tprint(i)')

st.subheader('Checkbox')
st.checkbox('Male')                                # Checkbox
if(st.checkbox('Female')):                          # Checkbox with Validation
    st.write("you're an Female")

st.subheader('RadioButton')
radioButton = st.radio('Select : ',('Male','Female','Other'))      # RadioButton
if(radioButton == 'Male'):
    st.write("you're a male")
elif(radioButton == 'Female'):
    st.write("you're a female")
elif(radioButton == 'Other'):
    st.write("you're a other gender")

st.subheader('Select Box')                                          # SelectBox
selectBox =  st.selectbox("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
st.write("you're selected : ",selectBox)

st.subheader('MultiSelect Box')                                   # MultiSelectBox
multiSelBox = st.multiselect("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                    'Deep Learning','Natural Language Processing',
                                                    'Computer Vision','Image Processing'])
st.write("You've selected : ", len(multiSelBox) , 'courses')


st.subheader('Button')                                             # Button
if(st.button('click me')):
    st.write('Thanks for clicking me')


st.subheader("Slider")                                             # Slider
vol = st.slider('Select the volume',0,100,step = 1)
st.write('Volume is : ',vol)

st.subheader("Text Input")                                        # Text-Input
username = st.text_input('Username : ')
password = st.text_input('Password : ', type = 'password')

st.subheader("Text Area")                                         # Text-Area
st.text_area('Write something interesting about yourself')

st.subheader("Input Number")                                      # Input-Number
st.number_input('Select your age',18,110)

st.subheader("Input Date")                                       # Input-Date
st.date_input('Date')

st.subheader("Input Time")                                       # Input-Time
st.time_input('Time')
