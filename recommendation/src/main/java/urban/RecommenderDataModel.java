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

    /**
     * User id, Course id, Grade
     * + some other questions to understand better the users:
     *
     * 1000 = want to receive newsletter about course X
     * 1001 = want to receive newsletter about course Y
     * 1002 = want to receive newsletter about course Z
     *
     * between 0(no) and 1(yes)
     *
     * @return
     * @throws IOException
     */
    public DataModel getCoursesModel2() throws IOException {
        return getDataModel("courses2.csv");
    }

    private DataModel getDataModel(String pathname) throws IOException {
        File dataFile = new File("src/main/resources/" + pathname);
        return new FileDataModel(dataFile);
    }
}

