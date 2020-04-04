<template>
  <v-app>
    <v-card class="ma-9">
      <v-text-field name="url" label="url" v-model="url"></v-text-field>
      <v-form>
        <v-text-field name="title" label="title" v-model="title"></v-text-field>
        <v-text-field name="message" label="message" v-model="message"></v-text-field>
        <v-text-field
          name="img"
          label="img"
          v-model="img"
        ></v-text-field>
        <v-btn class="ma-4" color="success" @click="send()">send</v-btn>
      </v-form>
      <v-alert :value="Boolean(response)">{{response}}</v-alert>
    </v-card>
  </v-app>
</template>

<script>
// @ is an alias to /src
const axios = require("axios");

export default {
  name: "Home",
  data() {
    return {
      title: "",
      message: "",
      img: "",
      url: "http://192.168.0.54",
      response: ""
    };
  },
  methods: {
    send() {
      let data = {
        title: this.title,
        message: this.message,
        imgurl: this.img
      };
      console.log(data)
      let self = this;
      let url = this.url + ":8000";
      axios.post(url, data).then(function(response) {
        self.response = response.data;
      });
    }
  }
};
</script>
