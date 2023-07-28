<script setup lang="ts">

import { ref } from "vue";
import PromptField from 'src/models/User/components/PromptField/PromptField.vue';

const API_URL = 'http://127.0.0.1:5000'

let input = ref('');
let output = ref('');

const submit = () => {
  fetch(`${API_URL}/chat`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "prompt": input.value
    },
  })
  .then(res => res.json())
  .then(res => output.value = res.content)

  input.value = ''

}

</script>

<template>
  <q-page class="row items-center justify-evenly">

    <q-card class="bg-grey-9" style="width: 50vw; height: 50vh; display: flex; flex-direction: column;">
      <q-card-section>
        <div class="text-h3">Chat</div>
      </q-card-section>

      <q-card-section class="flex grow-1">
        <span>{{ output }}</span>
      </q-card-section>

      <q-card-actions>
        <form @submit.prevent="submit" style="width: 100%">
          <PromptField v-model="input" :submit="submit" />
        </form>
      </q-card-actions>

    </q-card>
  </q-page>
</template>
