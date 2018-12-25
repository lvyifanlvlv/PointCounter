class AddStudentnameToCounters < ActiveRecord::Migration[5.2]
  def change
    add_column :counters, :studentname, :string
  end
end
