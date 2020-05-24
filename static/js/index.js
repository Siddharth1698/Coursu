var firebaseConfig = {
  apiKey: "AIzaSyAxY9OQgRkhm2ygYrv-DWoUnoP4eWM0h-8",
  authDomain: "coursu-1870c.firebaseapp.com",
  databaseURL: "https://coursu-1870c.firebaseio.com",
  projectId: "coursu-1870c",
  storageBucket: "coursu-1870c.appspot.com",
  messagingSenderId: "1080098103447",
  appId: "1:1080098103447:web:8ae6ed2890f9f77bfc49d2",
  measurementId: "G-YCRY4MD1PT"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();


firebase.auth.Auth.Persistence.LOCAL;

$("#btn-login").click(function (){

  var email = $(this.#email).val();
  var password = $(this.#password).val();

  if (email != "" && password != ""){

    var result = firebase.auth().signInWithEmailAndPassword(email, password);
    result.catch(function (error){})
  
  }

  else {
    window.alert("not able to sign in");
  }



});
