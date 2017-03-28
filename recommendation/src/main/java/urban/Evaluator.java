package urban;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.eval.RecommenderBuilder;
import org.apache.mahout.cf.taste.impl.eval.AverageAbsoluteDifferenceRecommenderEvaluator;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.common.RandomUtils;

import java.io.IOException;

public class Evaluator {

    public static void main(String[] args) throws IOException, TasteException {
        RandomUtils.useTestSeed(); // fixing training and test samples

        //DataModel model = new RecommenderDataModel().getProductsModel();
        DataModel model = new RecommenderDataModel().getCoursesModel();

        AverageAbsoluteDifferenceRecommenderEvaluator evaluator = new AverageAbsoluteDifferenceRecommenderEvaluator();
        RecommenderBuilder builder = new MyRecommenderBuilder();

        double error = evaluator.evaluate(builder, null, model, 0.9, 1.0);
        System.out.println("Error average on every recommendation: " + error);
    }
}
