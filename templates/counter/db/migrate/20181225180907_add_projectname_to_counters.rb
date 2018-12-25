class AddProjectnameToCounters < ActiveRecord::Migration[5.2]
  def change
    add_column :counters, :projectname, :string
  end
end
