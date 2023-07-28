<script setup lang="ts">

import { ref } from 'vue';

import PromptField from 'models/User/components/PromptField/PromptField.vue';
const API_URL = 'http://127.0.0.1:5000'


let input = ref('');
let output = ref('');
let file = ref(null);
let loading = ref(false);

const submit = () => {
  // console.log(file)
  loading.value = true;

  const formData = new FormData();
  formData.append('file', file.value);
  formData.append('prompt', input.value);

  fetch(`${API_URL}/blip`, { method: "POST", body: formData })
    .then(res => res.json())
    .then(res => output.value = res)
    .then(() => loading.value = false)
    .catch(err => console.log(err))

  input.value = '';
}
</script>

<template dark>
  <q-page class="row items-center justify-evenly">
    <q-card class="bg-grey-9" style="width: 50vw; height: 50vh; display: flex; flex-direction: column;">
      <q-card-section>
        <div class="text-h3">Blip-2</div>
      </q-card-section>

      <q-card-section style="height: 100%;">
        <div v-if="!loading">{{ output }}</div>

        <div v-if="loading" class="row items-center justify-evenly" style="width: 100%; height: 100%;">
          <q-spinner size="10rem" :thickness="1" />
        </div>
      </q-card-section>

      <q-card-actions class="q-gutter-sm flex flex-direction-column">
        <q-file dark outlined v-model="file" label="Choose file" class="flex grow-1">
          <template v-slot:append>
            <q-btn flat round icon="attach_file" />
          </template>
        </q-file>
        <form @submit.prevent="submit" style="width: 100%;">
          <PromptField v-model="input" :submit="submit" />
        </form>
      </q-card-actions>
    </q-card>
  </q-page>
</template>
