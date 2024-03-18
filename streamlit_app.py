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
               ['Local Spotlight','Superhero','#TransRightsReadathon','Humor','Media Tie Ins'], [])

 
button_books = st.button("Get Books")

st.divider()

  # Update values for recommendation
fiction = 1 if question1 == 'Fiction' else 0
fiction2 = 1 if question1 == 'Fiction' else 0
reader_adult = 1 if 'Adult' in question6 else 0
reader_ya = 1 if 'YA' in question6 else 0
mc_male = 1 if 'Male (includes ftm)' in question4 else 0
mc_female = 1 if 'Female (includes mtf)' in question4 else 0
mc_nb = 1 if 'Non-Binary' in question4 else 0
genre_fantasy = 1 if 'Fantasy' in question3 else 0
genre_romance = 1 if 'Romance' in question3 else 0
genre_scifi = 1 if 'Sci-Fi' in question3 else 0
genre_historical = 1 if 'Historical' in question3 else 0
genre_horror = 1 if 'Horror' in question3 else 0
genre_mystery = 1 if 'Mystery' in question3 else 0
genre_nf = 1 if question1 == 'NonFiction' else 0
genre_nf2 = 1 if question1 == 'Nonfiction' else 0
lgbt_wlw = 1 if any(item in ['WLW', 'Any LGBT+'] for item in question7) else 0 
lgbt_mlm = 1 if any(item in['MLM', 'Any LGBT+']for item in question7) else 0
lgbt_nonb = 1 if any(item in['Nonbinary']for item in question7) else 0
lgbt_trans = 1 if any(item in['Transgender', 'Any LGBT+']for item in question7) else 0
lgbt_ace = 1 if any(item in['Asexual']for item in question7) else 0
lgbt_aro = 1 if any(item in['Aromantic']for item in question7) else 0
lgbt_mga = 1 if any(item in['Multi-Gender Attracted', 'Any LGBT+']for item in question7) else 0
read_vs = 1 if question5 == 'Very Short Read (<150 pages)' else 0
read_s = 1 if question5 =='Short Read (150-250 pages)' else 0
read_a = 1 if question5 == 'Average Read (250-350 pages)' else 0
read_l = 1 if question5 =='Long Read (350-425 pages)' else 0
read_vl = 1 if question5 == 'Very Long Read (>425 pages)' else 0
  
  #make dictionary with input values
input_dict = {
      "fiction": fiction,
      "fiction2": fiction2,
      "genre_fantasy":genre_fantasy,
      "genre_romance":genre_romance,
      "genre_scifi":genre_scifi,
  "genre_historical":genre_historical,
  "genre_horror":genre_horror,
  "genre_mystery":genre_mystery,
  "genre_nf":genre_nf,
  "genre_nf2":genre_nf2,
      "reader_adult":reader_adult,
      "reader_ya":reader_ya,
  "lgbt_wlw":lgbt_wlw,
  "lgbt_mlm":lgbt_mlm,
  "lgbt_nonb":lgbt_nonb,
  "lgbt_trans":lgbt_trans,
  "lgbt_ace":lgbt_ace,
  "lgbt_aro":lgbt_aro,
  "lgbt_mga":lgbt_mga,
  "mc_male": mc_male,
      "mc_female": mc_female,
      "mc_nb": mc_nb,
    "read_vs":read_vs,
    "read_s":read_s,
    "read_a":read_a,
    "read_l":read_l,
    "read_vl":read_vl}
  
 #make a df from the input dictionary
input_df = pd.DataFrame(input_dict, index=[0])
  
#start prediction code
#df_model = pd.read_csv('df_betterlengths.csv')
  
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
  #for i, (title, book_id, distance, author, summary, info) in enumerate(zip(nearest_neighbors_data['title'], nearest_neighbors_data['book_id'], nearest_neighbors_distances, nearest_neighbors_data['author'], nearest_neighbors_data['summary'], nearest_neighbors_data['info'])):
   # st.header(f" Match {i + 1}: ")
    #st.subheader(f"{title} \n_By: {author}_")
  #  st.write(f"{info}")
   # st.write(f"{summary}")
   # st.write(" ")
