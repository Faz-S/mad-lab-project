import { StyleSheet, Text, View ,Image,TextInput} from 'react-native'
import React from 'react'
import {styled} from 'nativewind'
import { Pressable, TouchableOpacity } from 'react-native-gesture-handler'
const Logo = require('../assets/left2.png');

const google = require('../assets/google.png')
const LoginScreen = ({navigation}) => {
  return (
    <View style={styles.container}className="flex w-full h-full bg-tertiary">
      <View className="px-5 items-center">
        <Text className="pt-14 pb-5 text-3xl" style={styles.heading}>Login</Text>
      </View>
      <TouchableOpacity  style={styles.text}className="pt-4 flex-row bg-black px-10 w-72 ml-8"
       activeOpacity={0.7} 
       >  
          <Image source={google} className="w-6 h-6 mb-4 ml-1"/>
          <Text style={styles.btntext} className="text-white pl-4">
            Continue with Google
          </Text>
        </TouchableOpacity>
      <View className="pt-5 px-4 flex-row">
        <Text className="font-black">_______________</Text>
        <Text className="px-2 pt-1" style={styles.subtext}>Or login with email</Text>
        <Text className="font-black">_______________</Text>
      </View>
      <View>
        {/* <TextInput placeholder='Enter Your Name' className="mx-9 mt-9 bg-white rounded-3xl pl-5 " style={styles.inputtxt}/> */}
        <TextInput placeholder='Enter Your Email' keyboardType='email-address' className="mx-9 mt-6 bg-white rounded-3xl pl-5 " style={styles.inputtxt}/>
        <TextInput keyboardType='visible-password' placeholder='Enter Your Password' className="mx-9 mt-6  bg-white rounded-3xl pl-5 " style={styles.inputtxt}/>
      </View>
      <View className="pt-3 flex-row">
        
        
        <View>
          
          <View style={styles.textbtn} className="ml-28 mt-2">
            <TouchableOpacity  className="bg-black w-32 mt-3 p-2 rounded-3xl"
            activeOpacity={0.7} 
            onPress={()=>{
              navigation.navigate('Land')
            }}
            >  
              {/* <Image source={google} className="w-6 h-6 mb-4 ml-1"/> */}
              <Text style={styles.btntext2} className="text-white text-center ">
                  Login
              </Text>
            </TouchableOpacity>
            <View>
              <Text style={styles.btntext2} className="mt-4 -ml-3 ">Dont have an account?</Text>
              <TouchableOpacity
          onPress={()=>{
            navigation.navigate('Signup')
          }}
          activeOpacity={0.7}
          >
              <Text style={styles.btntext3} className="ml-10">
                Sign Up
              </Text>
         

          </TouchableOpacity
            
          >
          <Image source={Logo} className="w-80 h-80 -ml-24" style={styles.img}/>
          
            </View>
            
        </View>
        </View>
        </View>
      </View>
    
  )
}

export default LoginScreen

const styles = StyleSheet.create({
  container:{
    
  },
  heading:{
    fontFamily:"Poppins-Bold",
    letterSpacing:1,
    
  },
  btntext:{
    fontFamily:"Poppins-Bold",
    fontSize:16,
  },
  text:{
    borderRadius:40,
  
  },
  subtext:{
    fontFamily:"Poppins-Bold",
  },
  inputtxt:{
    fontFamily:"Poppins-Bold",
    fontSize:14,
    paddingLeft:20,
    paddingRight:20,
    
    backgroundColor:"#F5F5F5",
    borderRadius:20,
    height:40,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
  },
  
  btntext2:{
    fontFamily:"Poppins-Bold",
    fontSize:14,
    
  },
  btntext3:{
    fontFamily:"Poppins-Bold",
    fontSize:14,
    color:"#e63946",
    
  }
})