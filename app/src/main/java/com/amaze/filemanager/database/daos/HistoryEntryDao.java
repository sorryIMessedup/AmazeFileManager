package com.amaze.filemanager.database.daos;

import androidx.room.Dao;
import androidx.room.Insert;
import androidx.room.OnConflictStrategy;
import androidx.room.Query;
import androidx.room.Update;

import com.amaze.filemanager.database.models.utilities.History;

import static com.amaze.filemanager.database.UtilitiesDatabase.COLUMN_PATH;
import static com.amaze.filemanager.database.UtilitiesDatabase.TABLE_HISTORY;

/**
 * {@link Dao} interface definition for {@link History}. Concrete class is generated by Room
 * during build.
 *
 * @see Dao
 * @see History
 * @see com.amaze.filemanager.database.UtilitiesDatabase
 */
@Dao
public interface HistoryEntryDao {

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    public void insert(History instance);

    @Update
    public void update(History instance);

    @Query("SELECT * FROM " + TABLE_HISTORY)
    public History[] list();

    @Query("DELETE FROM " + TABLE_HISTORY + " WHERE " + COLUMN_PATH + " = :path")
    public void deleteByPath(String path);

    @Query("DELETE FROM " + TABLE_HISTORY)
    public void clear();
}
