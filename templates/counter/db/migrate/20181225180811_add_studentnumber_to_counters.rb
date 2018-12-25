class AddStudentnumberToCounters < ActiveRecord::Migration[5.2]
  def change
    add_column :counters, :studentnumber, :string
  end
end
