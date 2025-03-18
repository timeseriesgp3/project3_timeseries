#!/bin/bash
# Create a Streamlit configuration directory if it doesn't exist
mkdir -p ~/.streamlit/

# Write the Streamlit configuration file
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
