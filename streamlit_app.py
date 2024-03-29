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
st.write("This is currently only for the Prose Collection")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
  question7= st.multiselect("**What kind of media?**",
            ['Prose', 'Poetry', 'Anthology'], [])
  question6 = st.selectbox("**Target Reader Age**",
            ('','Adult','Kids'))
with col2:
  question1 = st.selectbox("**Fiction or NonFiction?**",
            ('','Fiction', 'Non-Fiction'))
  question5 = st.multiselect("**LGBT Representation**",
               ['Queer','#TransRightsReadathon'],[])
with col3:
  question3 = st.multiselect("**Genre**",
            ['Fantasy', 'Romance', 'Sci-Fi', 'Mystery','Historical','Horror', 'Drama'], [])
  question4 = st.multiselect("**Misc Collections**",
               ['Local Spotlight','Superhero','Humor','Media Tie Ins'], [])

button_books = st.button("Get Books")

st.divider()

  # Update values for recommendation
media_prose = 1 if 'Prose' in question7 else 0
media_poetry = 1 if 'Poetry' in question7 else 0
media_anthology = 1 if 'Anthology' in question7 else 0
audience_kids = 1 if question6 =='Kids' else 0
audience_adults = 1 if question6 =='Adult' else 0
nonfiction = 1 if question1 =='Non-fiction' else 0
lgbt_rep = 1 if any(item in ['Queer', '#TransRightsReadathon'] for item in question5) else 0
genre_fantasy = 1 if 'Fantasy' in question3 else 0
genre_horror = 1 if 'Horror' in question3 else 0
genre_romance = 1 if 'Romance' in question3 else 0
genre_drama = 1 if 'Drama' in question3 else 0
genre_historical = 1 if 'Historical' in question3 else 0
genre_scifi = 1 if 'Sci-Fi' in question3 else 0
genre_mystery = 1 if 'Mystery' in question3 else 0
misc_local = 1 if 'Local Spotlight' in question4 else 0
misc_hero = 1 if 'Superhero' in question4 else 0
misc_trans  = 1 if '#TransRightsReadathon' in question5 else 0
misc_humor = 1 if 'Humor' in question4 else 0
misc_mediatiein  = 1 if 'Media Tie Ins' in question4 else 0

  
  #make dictionary with input values
input_dict = {
  'media_prose': media_prose, 
  'media_poetry': media_poetry, 
  'media_anthology': media_anthology, 
  'audience_kids':audience_kids, 
  'audience_adults':audience_adults, 
  'genre_fantasy': genre_fantasy, 
  'genre_horror': genre_horror, 
  'genre_romance': genre_romance, 
  'genre_drama': genre_drama,
  'genre_historical': genre_historical,
  'genre_scifi':genre_scifi,
  'genre_mystery': genre_mystery,
  'lgbt_rep':lgbt_rep,
  'nonfiction':nonfiction,
  'misc_local':misc_local,
  'misc_hero':misc_hero,
  'misc_trans':misc_trans,
  'misc_humor':misc_humor,
  'misc_mediatiein':misc_mediatiein}
  
 #make a df from the input dictionary
input_df = pd.DataFrame(input_dict, index=[0])
  
#start prediction code
df_model = pd.read_csv('df_model.csv')
  
features = df_model[['media_prose', 'media_poetry', 'media_anthology', 'audience_kids', 'audience_adults', 
               'genre_fantasy', 'genre_horror', 'genre_romance', 'genre_drama', 'genre_historical', 'genre_scifi', 
               'genre_mystery', 'lbgt_rep', 'nonfiction', 'misc_local', 'misc_hero', 'misc_trans', 'misc_humor', 
               'misc_mediatiein']].values

knn = NearestNeighbors(n_neighbors=10, metric='euclidean')
knn.fit(features)  # get the model
selected_book = input_df.values.tolist()
distances, indices = knn.kneighbors(selected_book)
 
nearest_neighbors_distances = distances[0]
nearest_neighbors_data = df_model.iloc[indices[0]]
  
if button_books:
  for i, (Title, URL, distance, Summary, Collections, Price) in enumerate(zip(nearest_neighbors_data['Title'], nearest_neighbors_data['URL'], nearest_neighbors_distances, nearest_neighbors_data['Summary'], nearest_neighbors_data['Collections'], nearest_neighbors_data['Price'])):
    st.header(f" Match {i + 1}: ")
    st.subheader(f"{Title} \n_{URL}_ {Price}")
    st.write(f"{Collections}")
    st.write(f"{Summary}")
    st.write(" ")
