import streamlit as st
from PIL import Image
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import altair as alt

st.set_page_config(page_title="Dreamer's & Make-Believers", page_icon="📚", layout="centered")

image1 = Image.open('Logo.jpeg')
st.image(image1)
st.write("Fill in at least 3 fields for the best results")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
  question7= st.multiselect("**What kind of media**",
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
media_prose = 1 if question7 == 'Prose' else 0
media_poetry = 1 if question7 == 'Poetry' else 0
media_anthology = 1 if question7 == 'Anthology' else 0
audience_kids = 1 if question6 =='Kids' else 0
audience_adults = 1 if question6 =='Adult' else 0
nonfiction = 1 if question1 =='Non-fiction' else 0
lbgt_rep = 1 if any(item in ['Queer', '#TransRightsReadathon'] for item in question5) else 0
genre_fantasy = 1 if question3 =='Fantasy' else 0
genre_horror = 1 if question3 =='Horror' else 0
genre_romance = 1 if question3 =='Romance' else 0
genre_drama = 1 if question3 =='Drama' else 0
genre_historical = 1 if question3 =='Historical' else 0
genre_scifi = 1 if question3 =='Sci-Fi' else 0
genre_mystery = 1 if question3 =='Mystery' else 0
misc_local = 1 if question4=='Local Spotlight' else 0
misc_hero = 1 if question4=='Superhero' else 0
misc_trans = 1 if question1=='#TransRightsReadathon' else 0
misc_humor = 1 if question4=='Humor' else 0
misc_mediatiein = 1 if question4=='Media Tie Ins' else 0

  
  #make dictionary with input values
input_dict = {
  'media_prose': media_prose, 
  'media_poetry': media_poetry, 
  'media_anthology': media_anthology, 
  'audience_kids':audience_kids, 
  'audience_adults':audience:adults, 
  'genre_fantasy': genre_fantasy, 
  'genre_horror': genre_horror, 
  'genre_romance': genre:romance, 
  'genre_drama': genre_drama,
  'genre_historical': genre_historical,
  'genre_scifi':genre_scifi,
  'genre_mystery': genre_mystery,
  'lbgt_rep':lgbt_rep,
  'nonfiction':nonfiction,
  'misc_local':misc_local,
  'misc_hero':misc_hero,
  'misc_trans':misc_trans,
  'misc_humor':misc_humor,
  'misc_mediatiein':misc_mediatiein}
  
 #make a df from the input dictionary
input_df = pd.DataFrame(input_dict, index=[0])
  
#start prediction code
#df_model = pd.read_csv('df_model.csv')
  
#features = df_model[['fiction','fiction2','genre_fantasy', 'genre_romance',
 #                 'genre_sci-fi', 'genre_historical','genre_horror','genre_mystery', 'genre_nf','genre_nf2','reader_adult', 'reader_ya',
  #                'lgbt_wlw', 'lgbt_mlm','lgbt_nonb', 'lgbt_trans', 'lgbt_ace', 'lgbt_aro', 'lgbt_mga', 'mc_male', 'mc_female','mc_nb', 'read_vs',
   #               'read_s', 'read_a','read_l','read_vl']].values

#knn = NearestNeighbors(n_neighbors=10, metric='euclidean')
#knn.fit(features)  # get the model
#selected_book = input_df.values.tolist()
#distances, indices = knn.kneighbors(selected_book)
 
#nearest_neighbors_distances = distances[0]
#nearest_neighbors_data = df_model.iloc[indices[0]]
  
if button_books:
  st.write("It works :) ")
  st.write(input_df)
  #for i, (title, book_id, distance, author, summary, info) in enumerate(zip(nearest_neighbors_data['title'], nearest_neighbors_data['book_id'], nearest_neighbors_distances, nearest_neighbors_data['author'], nearest_neighbors_data['summary'], nearest_neighbors_data['info'])):
   # st.header(f" Match {i + 1}: ")
    #st.subheader(f"{title} \n_By: {author}_")
  #  st.write(f"{info}")
   # st.write(f"{summary}")
   # st.write(" ")
