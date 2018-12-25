class AddPictureToCounters < ActiveRecord::Migration[5.2]
  def change
    add_column :counters, :picture, :string
  end
end
