import pandas as pd
import numpy as np
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

def recommend(game):
    game_index = name[name['game_name'] == game].index[0]
    similarity = cosine_similarity(np.array(df_preprocessed.iloc[game_index]).reshape(1, -1), df_preprocessed)
    index = similarity[0].argsort()[-2:-7:-1]
    return name.loc[index,'game_name'].values,name.loc[index,'url'].values,name.loc[index,'img_url'].values


st.header('Game Recommender System')
df_preprocessed=pd.read_csv("df_preprocessed.csv")
name=pd.read_csv("name.csv")

game_list = name['game_name'].values
selected_game = st.selectbox(
    "Type or select a game from the dropdown",
    game_list
)

if st.button('Show Recommendation'):
    recommended_game_names,recommended_game_url,recommended_game_posters = recommend(selected_game)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        # st.image(recommended_game_posters[0],use_column_width='always', caption=recommended_game_names[0]) old version
        st.markdown(f'''
                    <a href={recommended_game_url[0]}>
                        <img src={recommended_game_posters[0]} />
                        <p>{recommended_game_names[0]}</p>
                    </a>''',
                    unsafe_allow_html=True
                    )
    with col2:
        st.markdown(f'''
                    <a href={recommended_game_url[1]}>
                        <img src={recommended_game_posters[1]} />
                        <p>{recommended_game_names[1]}</p>
                    </a>''',
                    unsafe_allow_html=True
                    )
    with col3:
        st.markdown(f'''
                    <a href={recommended_game_url[2]}>
                        <img src={recommended_game_posters[2]} />
                        <p>{recommended_game_names[2]}</p>
                    </a>''',
                    unsafe_allow_html=True
                    )
    with col4:
        st.markdown(f'''
                    <a href={recommended_game_url[3]}>
                        <img src={recommended_game_posters[3]} />
                        <p>{recommended_game_names[3]}</p>
                    </a>''',
                    unsafe_allow_html=True
                    )
    with col5:
        st.markdown(f'''
            <a href={recommended_game_url[4]}>
                <img src={recommended_game_posters[4]} />
                <p>{recommended_game_names[4]}</p>
            </a>''',
                    unsafe_allow_html=True
                    )
