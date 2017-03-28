package urban;

import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.model.DataModel;

import java.io.File;
import java.io.IOException;

public class RecommenderDataModel {

    /**
     * User id, Product id, Grade
     *
     * @return
     * @throws IOException
     */
    public DataModel getProductsModel() throws IOException {
        return getDataModel("data.csv");
    }

    /**
     * User id, Course id, Grade
     *
     * @return
     * @throws IOException
     */
    public DataModel getCoursesModel() throws IOException {
        return getDataModel("courses.csv");
    }

    private DataModel getDataModel(String pathname) throws IOException {
        File dataFile = new File(pathname);
        return new FileDataModel(dataFile);
    }
}

