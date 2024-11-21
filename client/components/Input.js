import React from 'react'
import { StyleSheet, Text, TextInput, View } from 'react-native';

const Input = ({style,value,placeholder,onChange}) => {
  return (
    <View>
      <TextInput style={style} value={value} placeholder={placeholder} onChange={onChange}/>
    </View>
  )
}

export default Input
