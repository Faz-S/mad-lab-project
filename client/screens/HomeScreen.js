import React,{useState} from 'react'
import { StyleSheet, Text, View ,Image, Pressable } from 'react-native'
import {styled } from 'nativewind'
import { TouchableOpacity } from 'react-native-gesture-handler';

const applogo= require('../assets/SelfieDoodle.png');
const HomeScreen = ({navigation}) => {
    // const [homeScreen,setHomeScreen]=useState('')
  return (
    <View className="flex w-full h-full justify-between bg-tertiary">
        <View className="px-5 items-center"> 
          <Text style={styles.heading} className="pt-14 pb-1">
            Welcome to Verbiqube
          </Text>
          <Text style={styles.text} className="text-lightblack text-xl text-center pt-1">The perfect way to automate your Social media</Text>
          
       </View>

       <View className="flex">
          <Image source={applogo} className="w-80 h-80 ml-4"/>
       </View>
       <TouchableOpacity  className="items-center mx-5 pb-10 "
       activeOpacity={0.7} 
       onPress={()=>{navigation.navigate("Signup")}}
       >
        <Text style={styles.btntext} className="text-white bg-black text-xl text-center rounded-xl w-full p-5">
           Get Started
          </Text>
        </TouchableOpacity>
       
    </View>
  )
}

export default HomeScreen

const styles = StyleSheet.create({
    heading: {
        fontFamily: 'Poppins-Bold',
        fontSize: 27,
      },
      text: {
        fontFamily: 'Poppins-Regular',
        // fontSize: 24,
      },
      btntext:{
        fontFamily: 'Poppins-Bold',
      },
     
});