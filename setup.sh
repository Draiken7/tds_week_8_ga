mkdir -p ~/.tds_week_8/

echo "\
[general]\n\
email = \"21f2000602@ds.study.iitm.ac.in\"\n\
" > ~/.tds_week_8/creds.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.tds_week_8/config.toml
