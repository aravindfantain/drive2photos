import googleops 

iter = 0
limit = 9

def main():

    # try: 
    # service = drive_auth()

    # Create a session state variable to store the file & folder counts
    st.session_state["folder_count"] = 0
    st.session_state["image_file_count"] = 0
    st.session_state["video_file_count"] = 0
    st.session_state["other_file_count"] = 0

    with st.form("my_form"):
        top_level_folder = st.text_input('Enter the top level folder to start from')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            page_token = None
            folder = service.files().list(q="name='" + top_level_folder +"'",
                                            spaces='drive',
                                            fields='nextPageToken, '
                                                    'files(id, name)',
                                            pageToken=page_token).execute().get('files',[])[0]
            folder_id = folder.get('id')

            # with st.empty():
                # list_recursively(service, folder_id, top_level_folder)

    googleops.upload()
    

    # except:
        # e = sys.exc_info()[0]
        # TODO(developer) - Handle errors individually
        # st.write(f'An error occurred: {e}')
        # sys.exit()

def list_recursively(service, folder_id, folder_name):
    global iter
    global limit 

    iter += 1

    st.session_state['folder_count'] += 1

    page_token = None
    files = []
    while True:
        query = f"'{folder_id}' in parents"
        response = service.files().list(
            q = query,
            spaces='drive',
            fields='nextPageToken, '
                    'files(id, name, mimeType, parents)',
            pageToken=page_token).execute()
        for file in response.get('files', []):
            if file.get('mimeType') == 'application/vnd.google-apps.folder' and iter <= limit:
                # st.write('--------------------------------------')
                # st.write(F'Folder -> {file.get("name")}')
                list_recursively(service, file.get('id'), f'{folder_name} -> {file.get("name")}')
            else:
                f_name = file.get('name')
                f_mime_type = file.get('mimeType')
                if f_mime_type.startswith('image'):
                    f_type = 'IMAGE'
                    st.session_state['image_file_count'] += 1
                elif f_mime_type.startswith('video'):
                    f_type = 'VIDEO' 
                    st.session_state['video_file_count'] += 1
                else:
                    f_type = 'OTHER'
                    st.session_state['other_file_count'] += 1
                files.append({'id': file.get('id'), 'details': {'folder': folder_name, 'type': f_type, 'name' : f_name}})
                st.markdown(f"""
                    No. of folders: {st.session_state['folder_count']}  
                    No. of images: {st.session_state['image_file_count']}  
                    No. of videos: {st.session_state['video_file_count']}  
                    No. of others: {st.session_state['other_file_count']}
                            """)
                
        # if len(files) > 0:
            # st.write('--------------------------------------')
            # st.markdown(f"""
            #    :red[FOLDER: {folder_name}]
            # """)
            # for file in files:
            #     st.write(file)

        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break


if __name__ == '__main__':
    main()
