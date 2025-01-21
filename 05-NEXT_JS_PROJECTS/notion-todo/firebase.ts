// Import the functions you need from the SDKs you need
import { initializeApp, getApps, getApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCOlV8IEHmvXtlJFhdBD0inLoimn4TZ6Go",
  authDomain: "notion-todo-33594.firebaseapp.com",
  projectId: "notion-todo-33594",
  storageBucket: "notion-todo-33594.firebasestorage.app",
  messagingSenderId: "754735601292",
  appId: "1:754735601292:web:ef8c0bdf273e7b6616cda9",
  measurementId: "G-J3E7716B9Z"
};

// Initialize Firebase
const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApp();
const db = getFirestore(app);

export { db };
