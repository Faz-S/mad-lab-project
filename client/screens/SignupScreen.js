import { StyleSheet, Text, View ,Image,TextInput} from 'react-native'
import React from 'react'
import {styled} from 'nativewind'
import { Pressable, TouchableOpacity } from 'react-native-gesture-handler'
const Logo = require('../assets/doodle.png');

const google = require('../assets/google.png')
const SignupScreen = ({navigation}) => {
  return (
    <View style={styles.container} className="flex w-full h-full bg-tertiary">
      <View className="px-5 items-center">
        <Text className="pt-14 pb-5 text-3xl" style={styles.heading}>Signup</Text>
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
        <Text className="font-black">______________</Text>
        <Text className="px-2 pt-1" style={styles.subtext}>Or continue with email</Text>
        <Text className="font-black">______________</Text>
      </View>
      <View>
        <TextInput placeholder='Enter Your Name' className="mx-9 mt-9 bg-white rounded-3xl pl-5 " style={styles.inputtxt}/>
        <TextInput placeholder='Enter Your Email' keyboardType='email-address' className="mx-9 mt-6 bg-white rounded-3xl pl-5 " style={styles.inputtxt}/>
        <TextInput keyboardType='visible-password' placeholder='Enter Your Password' className="mx-9 mt-6  bg-white rounded-3xl pl-5 " style={styles.inputtxt}/>
      </View>
      <View className="pt-5
       flex-row">
        <View className="ml-28">
        <Image source={Logo} className="w-72 h-72 mt-24" style={styles.img}/>
        </View>
        <View style={styles.textbtn} >
        <TouchableOpacity  className="bg-black w-40 -ml-28 mt-3 p-2 rounded-3xl"
       activeOpacity={0.7} 
       >  
          
          <Text style={styles.btntext2} className="text-white text-center ">
           Sign in
          </Text>
        </TouchableOpacity>
        <View>
          <Text style={styles.btntext2} className="mt-4 -ml-28">Already have an account?</Text>
        </View>
        <View>
          <TouchableOpacity
          onPress={()=>{
            navigation.navigate('Login')
          }}
          activeOpacity={0.7}
          >
              <Text style={styles.btntext3} className="-ml-11">
                Login
              </Text>
          </TouchableOpacity
          >
        </View>
        </View>
       
      </View>
    </View>
  )
}

export default SignupScreen

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
  img:{
    marginLeft:-100,
  },
  textbtn:{
    marginLeft:-96,
    
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