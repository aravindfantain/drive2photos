// Custom scripts
$(document).ready(function () {

    showSpinner();
    $.get('http://127.0.0.1:5001/drive2photos-12345/us-central1/login', (data) => {
        $("#includeHTML").text(JSON.stringify(data));
        hideSpinner();
    });

    /*
    firebase.auth().onAuthStateChanged(user => {

        if (user) {
            $("#user-img").attr("src", user.photoURL);
            $("#user-name").text(user.displayName);

            $("#user-detail").show();
            $("#firebaseui-auth-container").hide();
            hideSpinner();
        }
        else {
            $("#user-detail").hide();
            $("#firebaseui-auth-container").show();
            hideSpinner();

            // Initialize the FirebaseUI Widget using Firebase.
            var ui = new firebaseui.auth.AuthUI(firebase.auth());

            scopes = [
                'https://www.googleapis.com/auth/drive.metadata.readonly',
                'https://www.googleapis.com/auth/photoslibrary.readonly',
                'https://www.googleapis.com/auth/photoslibrary.appendonly'
            ];

            var uiConfig = {
                callbacks: {
                    signInSuccessWithAuthResult: function (authResult, redirectUrl) {
                        // User successfully signed in.
                        // Return type determines whether we continue the redirect automatically
                        // or whether we leave that to developer to handle.
                        return true;
                    },
                    uiShown: function () {
                        // The widget is rendered.
                        // Hide the loader.
                        document.getElementById('auth_loader').style.display = 'none';
                    }
                },
                // Will use popup for IDP Providers sign-in flow instead of the default, redirect.
                signInFlow: 'popup',
                signInSuccessUrl: 'http://127.0.0.1:5005',
                signInOptions: [
                    // Leave the lines as is for the providers you want to offer your users.
                    {
                        provider: firebase.auth.GoogleAuthProvider.PROVIDER_ID,
                        scopes,
                        requireDisplayName: false,
                        customParameters: {
                            // Forces account selection even when one account
                            // is available.
                            prompt: 'select_account'
                        }
                    }
                ],
                // Terms of service url.
                tosUrl: '<your-tos-url>',
                // Privacy policy url.
                privacyPolicyUrl: '<your-privacy-policy-url>'
            };

            ui.start('#firebaseui-auth-container', uiConfig);

        }
    });

    $.get('http://127.0.0.1:5001/drive2photos-12345/us-central1/on_request_example', (data) => {
        $("#includeHTML").html(data);
    });
    */

});

// Login check
// showSpinner();
// $.get('http://127.0.0.1:5001/drive2photos-12345/us-central1/login', (data) => {
// console.log(data)
// })
// hideSpinner();

// Sign out
function signOut() {
    firebase.auth().signOut().then(() => {
        // Sign-out successful.
    }).catch((error) => {
        alert(`Error occurred while signing out: ${error}`);
    });
}

//Show / Hide spinner
function showSpinner() {
    $('.spinner').show();
}

function hideSpinner() {
    $('.spinner').hide();
}

// On button click, get value 
// of input control Show alert 
// message box 
$("#submitButton").click(function () {
    var inputString = $("#topFolderInput").val();
    alert(inputString);
});

