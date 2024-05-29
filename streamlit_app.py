import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import altair as alt

st.set_page_config(page_title="Dreamer's & Make-Believers", page_icon="📚", layout="centered")

image1 = Image.open('Logo.jpeg')
st.image(image1)
st.divider()
st.write("This system will always give you the 10 closet matches to what you enter (It's not a filter)")
st.write("This is currently only for the Prose and Graphic Novel Collections")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
  question7= st.selectbox("**What kind of media?**",
            ('','Prose', 'Illustrated Prose','Graphic Novel','Comics','Picture Books','Manga','Board Books'))
  question6 = st.selectbox("**Target Reader Age**",
            ('','Adult','Kids'))
with col2:
  question1 = st.selectbox("**Fiction or NonFiction?**",
            ('','Fiction', 'NonFiction'))
  question5 = st.multiselect("**LGBT Representation**",
               ['Queer','#TransRightsReadathon'],[])
with col3:
  question3 = st.multiselect("**Genre**",
            ['Fantasy', 'Romance', 'Sci-Fi', 'Mystery','Historical','Horror', 'Drama'], [])
  question4 = st.multiselect("**Misc Details**",
               ['Superhero','Humor','Action and Adventure'], [])

button_books = st.button("Get Books")

st.divider()

  # Update values for recommendation
media_prose = 1 if any(item in ['Prose', 'Illustrated Prose'] for item in question7) else 0 
media_graphnovel = 1 if 'Graphic Novel' in question7 else 0
media_picture = 1 if any(item in ['Picture Books', 'Board Books'] for item in question7) else 0 
media_manga = 1 if 'Manga' in question7 else 0
media_comics = 1 if 'Comics' in question7 else 0
audience_kids = 1 if question6 =='Kids' else 0
genre_fantasy = 1 if 'Fantasy' in question3 else 0
genre_horror = 1 if 'Horror' in question3 else 0
genre_romance = 1 if 'Romance' in question3 else 0
genre_drama = 1 if 'Drama' in question3 else 0
genre_historical = 1 if 'Historical' in question3 else 0
genre_scifi = 1 if 'Sci-Fi' in question3 else 0
genre_mystery = 1 if 'Mystery' in question3 else 0
misc_superhero = 1 if 'Superhero' in question4 else 0
misc_trans  = 1 if '#TransRightsReadathon' in question5 else 0
misc_humor = 1 if 'Humor' in question4 else 0
misc_actionadventure = 1 if 'Action and Adventure' in question4 else 0
misc_nonfiction = 1 if 'NonFiction' in question1 else 0
misc_queer = 1 if 'Queer' in question5 else 0

  
  #make dictionary with input values
input_dict = {
  'media_prose': media_prose,
  'media_graphnovel': media_graphnovel,
  'audience_kids':audience_kids, 
  'genre_fantasy': genre_fantasy, 
  'genre_horror': genre_horror, 
  'genre_romance': genre_romance, 
  'genre_drama': genre_drama,
  'genre_historical': genre_historical,
  'genre_scifi':genre_scifi,
  'genre_mystery': genre_mystery,
  'misc_trans' : misc_trans,
  'misc_superhero':misc_superhero,
  'misc_humor':misc_humor,
  'misc_actionadventure':misc_actionadventure,
  'misc_nonfiction':misc_nonfiction,
  'misc_queer':misc_queer,
  'media_manga':media_manga,
  'media_comics':media_comics,
  'media_picture':media_picture}
  
#make a df from the input dictionary
input_df = pd.DataFrame(input_dict, index=[0])
selected_book = input_df.values.tolist()

#start prediction code
model_df = pd.read_csv('gnp_df.csv')
  
features = model_df[['media_prose','media_graphnovel','audience_kids','genre_fantasy','genre_horror','genre_romance','genre_drama',
                    'genre_historical','genre_scifi','genre_mystery','misc_trans','misc_superhero',
                    'misc_humor','misc_actionadventure','misc_nonfiction','misc_queer','media_manga',
                    'media_comics','media_picture']].values

knn = NearestNeighbors(n_neighbors=10, metric='euclidean')
knn.fit(features)  # get the model
distances, indices = knn.kneighbors(selected_book)
 
nearest_neighbors_distances = distances[0]
nearest_neighbors_data = model_df.iloc[indices[0]]
  
if button_books:
  for i, (Title, URL, distance, Summary, Collections, Price) in enumerate(zip(nearest_neighbors_data['Title'], nearest_neighbors_data['URL'], nearest_neighbors_distances, nearest_neighbors_data['Summary'], nearest_neighbors_data['Collections'], nearest_neighbors_data['Price'])):
    st.header(f" Match {i + 1}: ")
    st.subheader(f"{Title} \n_{URL}_ {Price}")
    st.write(f"{Collections}")
    st.write(f"{Summary}")
    st.write(" ")

#sidebar testing info
#st.sidebar.image(image1)

sidebarbox1 = st.sidebar.selectbox(
    "**What media type?**",
    ("", "Graphic Novel", "Prose")
)
sidebarbox2 = st.sidebar.multiselect(
  "**Genre**",
  ['','Fantasy', 'Romance', 'Sci-Fi', 'Mystery','Historical','Horror', 'Drama']
)
sidebarbox3 = st.sidebar.selectbox(
    "**Fiction or Nonfiction?**",
    ("","Fiction", "NonFiction")
)
sidebarbox4 = st.sidebar.selectbox(
    "**Target Reader Age**",
    ("","Kids", "Adult")
)
sidebarbox5 = st.sidebar.multiselect(
    "**Misc Details**",
    ["",'Superhero','Humor','Action and Adventure']
)
sidebarbox6 = st.sidebar.multiselect(
    "**LGBT Representation**",
    ["",'Queer','#TransrightsReadathon']
)

button_sidebooks = st.sidebar.button("Get Recommendations")
