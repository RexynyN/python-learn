from winotify import Notification, audio

toast = Notification(app_id="RexynyN",
                     title="Super Notification",
                     msg="The World Is About To End!",
                     duration="long",
                    #  icon="path/to/image"
                     )

toast.add_actions(label="Enter the Realm", launch=r"C:\Users\Admin\Downloads")

toast.show()

