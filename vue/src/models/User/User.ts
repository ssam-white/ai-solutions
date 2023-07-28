import { Model } from 'pinia-orm'
import { Uid, Attr, BelongsTo } from 'pinia-orm/dist/decorators'

export default class User extends Model {
  static entity = 'users'
  static primaryKey = 'id'

  @Uid()
    id: string
}
