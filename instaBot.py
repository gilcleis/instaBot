import random
from instapy import InstaPy
from instapy import smart_run
import yaml
import os

current_path = os.path.abspath(os.path.dirname(__file__))
data = yaml.safe_load(open("%s/data.yaml" % (current_path)))

# login credentials
insta_username = data['username']
insta_password = data['password']
os.system('cls')
# restriction data
dont_likes = ['dick', 'squirt', 'gay', 'homo', '#fit', '#fitfam', '#fittips',
         '#abs', '#kids', '#children', '#child','sad', 'rain', 'depression',
         '[nazi', 'promoter','jew', 'judaism', '[muslim', '[islam', 'bangladesh',
         '[hijab', '[niqab', '[farright', '[rightwing','#conservative', 'death', 
         '#naked', '#sex', '#fight','racist','bozo','lula','bolso']
ignore_users = ['user1', 'user2', 'user3']

""" Prevent commenting on and unfollowing your good friends (the images will 
still be liked)...
"""
friends = ['friend1', 'friend2', 'friend3']

""" Prevent posts that contain...
"""
ignore_list = []

# TARGET data
hashtags = data['hashtags']
""" Set similar accounts and influencers from your niche to target...
"""
targets = data['targets']

""" Skip all business accounts, except from list given...
"""
target_business_categories = ['category1', 'category2', 'category3']

# COMMENT data
comments = ['Nice shot! :camera: @{}',   
        'Great :thumbsup:',
        'Nice :open_mouth:',       
        ':raised_hands: :camera: @{}',
        ]
characters = [u'😮', u'📸',u'👍',u'🔝',u'🆒']
mark = ['', ' @{}']
for comment in range(10):
    comment = ''.join(random.sample(characters, random.randint(1, 3))) 
    comment += ''.join(random.sample(mark, 1)) 
    comments.append(comment)

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                #   headless_browser=True,
                  disable_image_load=True,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # HEY HO LETS GO
    # general settings
    # targets1 = session.grab_following(username="gilclei", amount="full", live_match=False, store_locally=True)
    # targets2 = session.grab_followers ( username = "gilclei" , amount = "full" , live_match = False , store_locally = True )
    # targets = list(set(targets1) - set(targets2))
    # print(targets)
    # exit()
    os.system('cls')
    print(u'⛰ ⛏')
    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)
    session.set_ignore_users(ignore_users)
    session.set_simulation(enabled=True)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    # max_followers=7500,
                                    # max_following=3000,
                                    # min_followers=25,
                                    # min_following=25,
                                    min_posts=10)
    # session.set_skip_users(skip_private=True,
    #                    private_percentage=100,
    #                    skip_no_profile_pic=True,
    #                    no_profile_pic_percentage=100,
    #                    skip_business=False,
    #                    skip_non_business=False,
    #                    business_percentage=100,
    #                    skip_business_categories=[],
    #                    dont_skip_business_categories=[],
    #                    skip_bio_keyword=[],
    #                    mandatory_bio_keywords=[],
    #                    skip_public=False,
    #                    public_percentage=0)
    session.set_action_delays(enabled=True,
                          like=2,
                          comment=3,
                          follow=4.17,
                          story=4,
                          unfollow=28)
    session.set_skip_users(skip_private=False,
                           skip_no_profile_pic=True,
                           skip_business=False,
                           dont_skip_business_categories=[
                               target_business_categories])
    if data['do_likes']:
        session.set_do_like(enabled=True, percentage=90)
    if data['do_delimit_likings']:
        session.set_delimit_liking(enabled=True, max_likes=None, min_likes=10)
    if data['do_stories']:
        session.set_do_story(enabled = True, percentage = 70, simulate = True) 
    if data['do_comments']:
        session.set_do_comment(enabled=True, percentage=80,comment_liked_photo=True)
        session.set_comments(comments, media='Photo')
        session.set_delimit_commenting(enabled=True, max_comments=None, min_comments=10)
        # session.set_delimit_commenting(enabled=True, comments_mandatory_words=['cat', 'dog'])
    if data['do_follow']:
        session.set_do_follow(enabled=True, percentage=40, times=1)

    # activities

    # FOLLOW+INTERACTION on TARGETED accounts
    """ Select users form a list of a predefined targets...
    """
    number = random.randint(3, 5)

    random_targets = targets

    if len(targets) <= number:
        random_targets = targets

    else:
        random_targets = random.sample(targets, number)

    """ Interact with the chosen targets...
    """

    # exit()
    if data['user_interact']:
        session.interact_by_users ( random_targets , amount = 2 , randomize = False , media = 'Photo' ) 

    if data['do_hashtags']:
        print(u'⛰ ⛏')
        session.like_by_tags(hashtags, amount=10, interact=True)
    if data['do_follow_user_followers']:
        session.follow_user_followers(random_targets,
                                  amount=random.randint(30, 60),
                                  randomize=True, sleep_delay=600,
                                  interact=True)

    # UNFOLLOW activity
    if data['do_unfollow']:
        """ Unfollow nonfollowers after one day...
        """
        session.unfollow_users(amount=random.randint(75, 100),
                            nonFollowers=True,
                            style="FIFO",
                            unfollow_after=24 * 60 * 60, sleep_delay=600)

        """ Unfollow all users followed by InstaPy after one week to keep the 
        following-level clean...
        """
        session.unfollow_users(amount=random.randint(75, 100),
                            allFollowing=True,
                            style="FIFO",
                            unfollow_after=168 * 60 * 60, sleep_delay=600)

    """ Joining Engagement Pods...
    """
    session.join_pods()

"""
Have fun while optimizing for your purposes, Nuzzo
"""
