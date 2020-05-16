import streamlit as st 
from datetime import date

# Text/Title

st.title("Streamlit Tutorial")


# Image 
 
from PIL import Image

img = Image.open("oh.jpeg") 
st.image(img, width=400, caption='Cartoon image')

# SIDEBARS

st.sidebar.header("About")
st.text('I am a sidebar')

# Header / Subheader 
st.header("Title")


st.subheader("Sub Title")


# TEXT

st.text("Hello Strealit")


# Markdown 

st.markdown('## MARKDOWN HEADER')


# ERROR TEXT COLOR


st.success('Success')

st.info('Information!')

st.warning('error')

st.error('Danger')

st.exception("NameError('Name three not defined')")


# Get Help info 

st.help(range)


# More text

st.write("Text to write ")

st.write(range(10))

st.write(date.today())


# videos 

vid_file = open("/Users/adammcmurchie/Documents/Zoom/opener/toUpload.mp4", 'rb').read()
# vid_bytes = vid_file.read()

st.video(vid_file)

# Audio 

# audio_file = open("/Users/adammcmurchie/Documents/Zoom/opener/audio_only.m4a").read()
# st.audio(audio_file, format='audio/m4a')


# widget

if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding widget")

# Radio 

status = st.radio("What is your status?", ("Active","Inactive"))

# Linking

if status == 'Active':
	st.success("You are active")
else:
	st.info("You are not active")\

# Select box 

occupation = st.selectbox("Occupation", ["Programmer", "Plumber", "Doctor", "dictator"])

st.write("you selected ", occupation)

# MultiSelect

location = st.multiselect("Where do you work?", ("London","NewYork","Tokyo","Edinburgh"))

st.write("You selected", len(location), "locations ")

# Slider 

age = st.slider("what is your level?", 1,5)


# Button 

st.button("Simple Button")

if st.button("Tell me something"):
	st.text("Streamlit is cool")



# Text Input 

firstname = st.text_input("Enter your name", "enter here ")


# Check the text input 
if st.button("Submit"):
	if firstname == "enter here ":
		st.error("Please enter your name")
	else:
		result = firstname.title()
		st.success(result)


# Text Area
message = st.text_area("Enter your message", "enter here ")



st.text('showing json')
st.json({'name':"adam", 'gender':"male"})

# code

st.text('showing code ')
st.code('import pandas as pd')

# raw code 

with st.echo():
	# i am a comment
	import pandas as pd
	df = pd.DataFrame()

# progress bar 
import time
mybar = st.progress(0)
for p in range(10):
	mybar.progress(p+1)






# spinner 

with st.spinner("waiting.."):
	time.sleep(5)
st.success("Finished")






# functions 

@st.cache
def run_fxn():
	return range(100)


st.write(run_fxn())



# Baloons 

#st.balloons()

# Plot

st.pyplot()

# dataframes

st.dataframe(df)

# tables 

st.table(df)



# More info from here

st.text("You can get more information from here, https://www.youtube.com/watch?v=_9WiB2PDO7k")