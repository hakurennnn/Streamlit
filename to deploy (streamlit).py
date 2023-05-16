import streamlit as st
import numpy as np
import tensorflow as tf

st.markdown('<link rel'styles'>)

  def load_model():
    model=tf.keras.models.load_model('best_model.h5')
    return model
  model=load_model()
  )

  def main():
      st.title("My App")
    st.write("""#Testing""")


  if __name__ == '__main__':
      main()
