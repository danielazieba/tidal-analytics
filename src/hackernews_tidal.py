import requests
import time
from bs4 import BeautifulSoup


# converts character phrases i.e. '1 day ago' to standard time format
# TO DO: convert all submission/comment timestamps
def convert_timestamp(time_char):

	time_number = int(time_char[0])

	if 'year' in time_char:
		time_number = time_number * 365 * 24 * 60 * 60
	elif 'month' in time_char:
		time_number = time_number * 30 * 24 * 60 * 60
	elif 'day' in time_char:
		time_number = time_number * 24 * 60 * 60
	elif 'hour' in time_char:
		time_number = time_number * 60 * 60
	elif 'minute' in time_char:
		time_number = time_number * 60

	return(time.time() - time_number)

#called inside find_profile to process profile data
def get_profile_info(raw_info):
	wanted_info = [raw_info[1], raw_info[3], raw_info[5].strip(), raw_info[7].strip()]
	return wanted_info

#gathers data from profile url
def find_profile(user):

	# username on hackernews you want to pull data for
    user_data = [] # stores user data
    #user_data = [username, date created, karma, description]

	# gets HTML of hackernews user profile
    url = 'https://news.ycombinator.com/user?id=' + user
    response = requests.get(url)
    html = response.content

	# give HTML to BeautifulSoup to get user data
    soup = BeautifulSoup(html, "html.parser")
    user_info = soup.body.center.table.tr.find_next_siblings("tr")

	#searches through HTML to find user table
    profile_data = []
    for row in user_info[1].findAll('tr'):
	    for cell in row.findAll('td'):
	        profile_data.append(cell.text)

    user_data.append(get_profile_info(profile_data))

    return user_data

#grabs most recent page of hackernews submissions from url
def find_submissions(user):
	
    submissions = [[],[],[]] # stores submissions; maximum is most recent page of submissions
    # submissions = [[list of submission titles], [list of submission links], [list of dates posted]]
    
    url_submissions = 'https://news.ycombinator.com/submitted?id=' + user
    response = requests.get(url_submissions)
    html = response.content

    soup = BeautifulSoup(html, "html.parser")
    user_submissions = soup.find_all('a', attrs={"class": "storylink"})
    submissions_dates = soup.find_all('span', attrs={"class": "age"})
    count = 0
    for i in user_submissions:
	    submissions[0].append(i.text)
	    submissions[1].append(i['href'])
	    submissions[2].append(convert_timestamp(submissions_dates[count].text))
	    count += 1

    return submissions

#grabs most recent page of hackernews comments from url
def find_comments(user):

    comments = [[], []] #stores comments; maximum is most recent page of comments
    # comments = [[comments text], [date posted]]

    url_comments = 'https://news.ycombinator.com/threads?id=' + user
    response = requests.get(url_comments)
    html = response.content

    soup = BeautifulSoup(html, "html.parser")
    user_comments = soup.select('a[href="' + "user?id=" + user + '"]')
    comment_age = []

	#iterates through comments flagged with user to get comment post times
    for i in range(len(user_comments)):
		# has to manually search HTML tree for static comment structure because page sometimes displays different users' comments
        for j in range(10):
	        user_comments[i] = user_comments[i].next_sibling
	        if (j == 1):
	            comments[1].append(convert_timestamp(user_comments[i].text))
        comments[0].append(user_comments[i].next_element.next_element.span.text)

        return comments

#grabs most recent page of favorited hackernews submissions
def find_favorites(user):

    favorites = [[], []] #stores favorited submissions; maximum is most recent page of submissions
    # favorites = [[favorites titles], [favorites links]]

    url_favorites = 'https://news.ycombinator.com/favorites?id=' + user
    response = requests.get(url_favorites)
    html = response.content

    soup = BeautifulSoup(html, "html.parser")
    user_favorites = soup.find_all('a', attrs={"class": "storylink"})
    for i in user_favorites:
        favorites[0].append(i.text)
        favorites[1].append(i['href'])

    return favorites
