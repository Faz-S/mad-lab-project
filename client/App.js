import React, { useState } from 'react';
import { Text, View, StyleSheet,Image } from 'react-native';
import { useFonts } from 'expo-font';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

import HomeScreen from './screens/HomeScreen';
import AppLoading from 'expo-app-loading'; // Handles loading state
import LoginScreen from './screens/LoginScreen';
import SignupScreen from './screens/SignupScreen';
import LandingScreen from './screens/LandingScreen';
import LinkedInPostScreen from './screens/LinkedinPost';
const girl = require('./assets/girl.png')
const space = require('./assets/space.jpeg')
const doodle= require('./assets/doodle.png')


export default function App() {

  const Stack=createStackNavigator();
  const [fontsLoaded] = useFonts({
    'Poppins-Bold': require('./assets/fonts/Poppins-Bold.ttf'),
    'Poppins-Regular': require('./assets/fonts/Poppins-Regular.ttf'),
  });

  if (!fontsLoaded) {
    return <AppLoading />; // Keep the loading screen until fonts are loaded
  }

  return (
      // <View >
      
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Home">
          <Stack.Screen name="Home" component={HomeScreen} options={{headerShown:false}}/>
          <Stack.Screen name="Signup" component={SignupScreen} options={{headerShown:false}}/>
          <Stack.Screen name="Login" component={LoginScreen} options={{headerShown:false}}/>
          <Stack.Screen name="Land" component={LinkedInPostScreen} options={{headerShown:false}}/>
          {/* <Stack.Screen name="Linkedin" component={LinkedInPostScreen} options={{headerShown:false}}/> */}


          
        </Stack.Navigator>
      </NavigationContainer>
      // </View>
      
      
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
}
)

// import React from 'react';
// import { NavigationContainer } from '@react-navigation/native';
// import { createStackNavigator } from '@react-navigation/stack';
// import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
// import RoadSignDetection from './page/RoadSignDetection'
// import ImageView from './page/DisplayImage';
// import BarcodeScanner from './page/BarCodeScanning';
// import Exp1 from './page/exp1';
// import Exp2 from './page/exp2';
// import Exp3 from './page/exp3';
// import Exp4 from './page/exp4';
// import Exp5 from './page/exp5';
// import Exp6 from './page/exp6';

// const Stack = createStackNavigator();

// // Home Screen with buttons to navigate to different screens
// function HomeScreen({ navigation }) {
//   return (
//     <View style={styles.container}>
//       <Text style={styles.title}>Home Screen</Text>
//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => navigation.navigate('Screen4')}
//       >
//         <Text style={styles.buttonText}>EXP1</Text>
//       </TouchableOpacity>
//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => navigation.navigate('Screen5')}
//       >
//         <Text style={styles.buttonText}>EXP2</Text>
//       </TouchableOpacity>
//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => navigation.navigate('Screen6')}
//       >
//         <Text style={styles.buttonText}>EXP3</Text>
//       </TouchableOpacity>
//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => navigation.navigate('Screen7')}
//       >
//         <Text style={styles.buttonText}>EXP4</Text>
//       </TouchableOpacity>
//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => navigation.navigate('Screen8')}
//       >
//         <Text style={styles.buttonText}>EXP5</Text>
//       </TouchableOpacity>
//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => navigation.navigate('Screen9')}
//       >
//         <Text style={styles.buttonText}>EXP6</Text>
//       </TouchableOpacity>
//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => navigation.navigate('Screen1')}
//       >
//         <Text style={styles.buttonText}>OCR on road signs</Text>
//       </TouchableOpacity>

//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => navigation.navigate('Screen5')}
//       >
//         <Text style={styles.buttonText}>Image View</Text>
//       </TouchableOpacity>

//       <TouchableOpacity
//         style={styles.button}
//         onPress={() => navigation.navigate('Screen3')}
//       >
//         <Text style={styles.buttonText}>Detect BarCode</Text>
//       </TouchableOpacity>
//     </View>
//   );
// }



// // Main App Component
// export default function App() {
//   return (
//     <NavigationContainer>
//       <Stack.Navigator initialRouteName="Home">
//         <Stack.Screen name="Home" component={HomeScreen} />
//         <Stack.Screen name="Screen1" component={RoadSignDetection} />
//         <Stack.Screen name="Screen2" component={ImageView} />
//         <Stack.Screen name="Screen3" component={BarcodeScanner} />
//         <Stack.Screen name="Screen4" component={Exp1} />
//         <Stack.Screen name="Screen5" component={Exp2} />
//         <Stack.Screen name="Screen6" component={Exp3} />
//         <Stack.Screen name="Screen7" component={Exp4} />
//         <Stack.Screen name="Screen8" component={Exp5} />
//         <Stack.Screen name="Screen9" component={Exp6} />
//         {/* <Stack.Screen name="Screen9" component={BarcodeScanner} /> */}
//       </Stack.Navigator>
//     </NavigationContainer>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     justifyContent: 'center',
//     alignItems: 'center',
//     backgroundColor: '#f0f0f0',
//   },
//   title: {
//     fontSize: 24,
//     fontWeight: 'bold',
//     marginBottom: 20,
//   },
//   button: {
//     backgroundColor: '#007AFF',
//     padding: 15,
//     marginVertical: 10,
//     borderRadius: 10,
//   },
//   buttonText: {
//     color: '#fff',
//     fontSize: 16,
//   },
//   screenText: {
//     fontSize: 20,
//     color: '#333',
//   },
// });
