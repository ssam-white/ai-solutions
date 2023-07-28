<script setup lang="ts">
  import { ref, watch, getCurrentInstance } from 'vue';

  const props = defineProps({
    submit: {
      type: Function,
      required: false
    }
  })

  const input = ref('');

  const instance = getCurrentInstance();

  watch(input, (newValue) => {
    instance.emit('update:value', newValue);
  });

</script>

<template>
  <q-input dark outlined standout="none" v-model="input" Placeholder="Prompt..." class="flex grow-1">
    <template v-slot:append>
      <!-- <q-icon name="send" /> -->
      <q-btn flat round icon="send" @click="props.submit" />
    </template>
  </q-input>
</template>
