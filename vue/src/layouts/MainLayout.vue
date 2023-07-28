<script setup lang="ts" >

import { ref } from 'vue';

let tab = ref('home');

</script>

<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          AI Solutions
        </q-toolbar-title>

        <q-tabs v-model="tab">
          <q-route-tab no-caps name="home" label="Home" to="/" />
          <q-route-tab no-caps name="chat" label="Chat" to="/chat" />
          <q-route-tab no-caps name="blip" label="Blip" to="/blip" />
        </q-tabs>

        <q-space />
        <!-- <div>Quasar v{{ $q.version }}</div> -->

      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
