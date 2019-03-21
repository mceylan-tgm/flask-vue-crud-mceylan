<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>User</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.user-modal>Add User</button>
        <br><br>

        <!-- books table -->
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Username</th>
              <th scope="col">Email</th>
              <th scope="col">Image</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in user" :key="index">
              <td>{{ user.username }}</td>
              <td>{{ user.email }}</td>
              <td>
                <img :src="user.image" class="rounded-circle"
                     alt="Circle image" width="50" height="50"/>
              </td>
              <td>
                <button type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.user-update-modal
                        @click="editUser(user)">
                    Update
                </button>
                <button type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteUser(user)">
                    Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>

    <!-- add book modal -->
    <b-modal ref="addUserModal"
             id="user-modal"
            title="Add a new user"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-username-group"
                      label="Username:"
                      label-for="form-username-input">
            <b-form-input id="form-username-input"
                          type="text"
                          v-model="addUserForm.username"
                          required
                          placeholder="Enter Username">
            </b-form-input>
        </b-form-group>
        <b-form-group id="form-email-group"
                      label="Email:"
                      label-for="form-email-input">
          <b-form-input id="form-email-input"
                        type="text"
                        v-model="addUserForm.email"
                        required
                        placeholder="Enter email">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-image-group"
                      label="Image:"
                      label-for="form-image-input">
          <b-form-input id="form-image-input"
                        type="text"
                        v-model="addUserForm.image"
                        required
                        placeholder="Enter image">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="editUserModal"
             id="user-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-username-edit-group"
                      label="Username:"
                      label-for="form-username-edit-input">
          <b-form-input id="form-username-edit-input"
                        type="text"
                        v-model="editUserForm.username"
                        required
                        placeholder="Enter Username">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-email-edit-group"
                      label="Email:"
                      label-for="form-email-edit-input">
          <b-form-input id="form-email-edit-input"
                        type="text"
                        v-model="editUserForm.email"
                        required
                        placeholder="Enter email">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-image-group"
                      label="Image:"
                      label-for="form-image-input">
          <b-form-input id="form-image-input"
                        type="text"
                        v-model="editUserForm.image"
                        required
                        placeholder="Enter image">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      user: [],
      addUserForm: {
        username: '',
        email: '',
        image: '',
      },
      editUserForm: {
        username: '',
        email: '',
        image: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getUser() {
      const path = 'http://localhost:5000/user';
      axios.get(path, {
        auth: {
          username: 'mceylan',
          password: 'secret',
        } })
        .then((res) => {
          console.log('asd');
          this.user = res.data.user;
        })
        .catch((error) => {
          // eslint-disab le-next-line
          console.error(error);
        });
    },
    addUser(payload) {
      const path = 'http://localhost:5000/user';
      axios.post(path, payload, {
        auth: {
          username: 'mceylan',
          password: 'secret',
        } })
        .then(() => {
          this.getUser();
          this.message = 'User added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUser();
        });
    },
    updateUser(payload, userID) {
      const path = `http://localhost:5000/user/${userID}`;
      axios.put(path, payload, {
        auth: {
          username: 'mceylan',
          password: 'secret',
        } })
        .then(() => {
          this.getUser();
          this.message = 'User updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUser();
        });
    },
    removeUser(userID) {
      const path = `http://localhost:5000/user/${userID}`;
      axios.delete(path, {
        auth: {
          username: 'mceylan',
          password: 'secret',
        } })
        .then(() => {
          this.getUser();
          this.message = 'User removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUser();
        });
    },
    initForm() {
      this.addUserForm.username = '';
      this.addUserForm.email = '';
      this.addUserForm.image = '';
      this.editUserForm.username = '';
      this.editUserForm.email = '';
      this.editUserForm.image = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      const payload = {
        username: this.addUserForm.username,
        email: this.addUserForm.email,
        image: this.addUserForm.image, // property shorthand
      };
      this.addUser(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUserModal.hide();
      const payload = {
        username: this.editUserForm.username,
        email: this.editUserForm.email,
        image: this.editUserForm.image, // property shorthand
      };
      this.updateUser(payload, this.editUserForm.id);
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      this.initForm();
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUserModal.hide();
      this.initForm();
      this.getUser(); // why?
    },
    onDeleteUser(user) {
      this.removeUser(user.id);
    },
    editUser(user) {
      this.editUserForm = user;
    },
  },
  created() {
    this.getUser();
  },
};
</script>
