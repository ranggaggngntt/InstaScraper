import xlsxwriter
import instaloader

def InstaScrape(username, password, target):
    L = instaloader.Instaloader()
    L.login(username, password)

    profile = instaloader.Profile.from_username(L.context, target)
    print("Fetching followers of profile {}.".format(profile.username))
    followers = set(profile.get_followers())

    workbook = xlsxwriter.Workbook(target + '.xlsx')
    sheet = workbook.add_worksheet()

    sheet.write('A1', 'Username')
    sheet.write('B1', 'Post')
    sheet.write('C1', 'Following')
    row = 1
    for follower in followers:
        sheet.write(row, 0, follower.username)
        sheet.write(row, 1, str(follower.mediacount))
        sheet.write(row, 2, str(follower.followees))
        row += 1
    workbook.close()

if __name__ == '__main__':
    username = input('Username: ')
    password = input('Password: ')
    target = input('Target Scrape (username): ')

    InstaScrape(username, password, target)
