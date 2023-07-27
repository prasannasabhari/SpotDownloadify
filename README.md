<h1 align = "center" >SpotDownloadify <h1/>
  
# Description
This automation project is developed in Python and Flask to interact with Spotify API using OAuth to get access to the user's song playlist and then get those songs data to download the MP3 songs from Youtube. In Spotify Free, you can't download songs but this script will help you overcome this problem.

# Instruction
## Step 1: Install the required modules
```
pip install -r requirements.txt
```
## Step 2: Setup the redirect url and get the clientid and clientsecret
   * Go to [Spotify Developer](https://developer.spotify.com/) click "Dashboard", log in to your Spotify account then click create an app and give a name to it(any name you want).

  * Then copy your app **clientid** and **clientsecret** and paste in it the SpotifyOAuth object in the **create_sp_oauth()** inside of **SongApp.py**. Don't show anyone the **clientsecret** cause they can access to your data(Always keep the clientsecret private to you).

   * Then click "Setting" and add these links in the Redirect URI field: 
            <h5>1. http://localhost:5000/redirect</h5>
            <h5>2. http://localhost:5000/redirect/</h5>
            <h5>3. http://127.0.0.1:5000/redirect</h5>
            <h5>4. http://127.0.0.1:5000/redirect/</h5>
  *Doing this will help spotify know where to redirect the user back when the process gets done*

## Step 3: Run the SongApp.py with Flask
```
python SongApp.py
```
*This script will do the process of getting the user's song playlist data and store that in a ".csv" file.*

## Step 4: Run the DownloadMP3.py 
```
python DownloadMP3.py
```
*This script will do the downloading process of ".mp3" songs from youtube and stores them in a folder in the local machine.*