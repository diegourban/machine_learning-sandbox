package urban;

import org.apache.mahout.cf.taste.common.TasteException;
import org.apache.mahout.cf.taste.eval.RecommenderBuilder;
import org.apache.mahout.cf.taste.impl.eval.AverageAbsoluteDifferenceRecommenderEvaluator;
import org.apache.mahout.cf.taste.impl.model.file.FileDataModel;
import org.apache.mahout.cf.taste.model.DataModel;
import org.apache.mahout.common.RandomUtils;

import java.io.File;
import java.io.IOException;

public class Evaluator {

    public static void main(String[] args) throws IOException, TasteException {

        RandomUtils.useTestSeed(); // fixing training and test samples

        File dataFile = new File("data.csv");
        DataModel dataModel = new FileDataModel(dataFile);

        AverageAbsoluteDifferenceRecommenderEvaluator evaluator = new AverageAbsoluteDifferenceRecommenderEvaluator();
        RecommenderBuilder builder = new ProductRecommenderBuilder();

        double error = evaluator.evaluate(builder, null, dataModel, 0.9, 1.0);

        System.out.println(error);
    }
}
