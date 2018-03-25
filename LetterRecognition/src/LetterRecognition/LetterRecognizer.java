package LetterRecognition;

import java.text.DecimalFormat;
import java.util.Arrays;

import neural.feedforward.FeedforwardLayer;
import neural.feedforward.FeedforwardNetwork;
import neural.feedforward.train.Train;
import neural.feedforward.train.backpropagation.Backpropagation;

import org.jfree.chart.JFreeChart;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileFilter;
import java.io.IOException;
import java.io.InputStreamReader;

import javax.imageio.ImageIO;

import org.apache.commons.io.filefilter.HiddenFileFilter;

public class LetterRecognizer {
	
	static double[][] input;
	static double[][] idealOutput = {
			/* A      a      B      b      C      c      D      d*/
			{0.00},{0.00},{0.04},{0.04},{0.08},{0.08},{0.12},{0.12},
			/* E      e      F      f      G      g      H      h */
			{0.16},{0.16},{0.20},{0.20},{0.24},{0.24},{0.28},{0.28},
			/* I      i      J      j      K      k      L      l*/
			{0.32},{0.32},{0.36},{0.36},{0.40},{0.40},{0.44},{0.44},
			/* M      m      N      n      O      o      P      p*/
			{0.48},{0.48},{0.52},{0.52},{0.56},{0.56},{0.60},{0.60},
			/* Q      q      R      r      S      s      T      t*/
			{0.64},{0.64},{0.68},{0.68},{0.72},{0.72},{0.76},{0.76},
			/* U      u      V      v      W      w      X      x*/
			{0.80},{0.80},{0.84},{0.84},{0.88},{0.88},{0.92},{0.92},
			/* Y     y      Z     z*/
			{0.96},{0.96},{1.0},{1.0}
		};
	
	public static void main(final String args[]) throws IOException {
		
		/* Images to Binary Images */
		System.out.println("Converting Images to Binary Images...");
		createDataSet();
		System.out.println("Conversion Completed!!!");
		
		/* Neural Network Setup */
		int inputNeurons = input[0].length;
		int outputNeurons = 1;
		InputStreamReader prompt = new InputStreamReader(System.in);
		BufferedReader inputReader = new BufferedReader(prompt);
		System.out.println("Constructing Neural Network: ");
		System.out.println("Input Layer Neurons: " + inputNeurons);
		System.out.println("Set Hidden Layer's Neurons: ");
		int hiddenNeurons = Integer.parseInt(inputReader.readLine()); 
		final FeedforwardNetwork network = new FeedforwardNetwork();
		System.out.println("Hidden Layer Neurons: " + hiddenNeurons);
		System.out.println("Output Layer Neurons: " + outputNeurons);
		/* Input Layer */
		network.addLayer(new FeedforwardLayer(inputNeurons));
		/* Hidden Middle Layer */ 
		network.addLayer(new FeedforwardLayer(hiddenNeurons));
		/* Output Layer */
		network.addLayer(new FeedforwardLayer(outputNeurons));
		network.reset();
		System.out.println("Neural Network Construction Succesfully Done!");
		System.out.println();
		
		/* Training Session */
		System.out.println("Preparing Training Session...");
		Chronometer chronometer = new Chronometer();
		chronometer.start();
		System.out.println("Set Learning Rate: ");
		double learningRate = Double.parseDouble(inputReader.readLine());
		System.out.println("Set Momentum: ");
		double momentum = Double.parseDouble(inputReader.readLine());
		
		System.out.println();
		System.out.println("Starting Training Session ( Threshold Error Value : 0,001 ) ... ");
		final Train train = new Backpropagation(network, input, idealOutput, learningRate, momentum);
		int epoch = 1;
		XYSeries series = new XYSeries("Error Value");
		do {
			train.iteration();
			series.add(epoch, train.getError());
			System.out.println("Epoch #" + epoch + " Error: " + train.getError());
			epoch++;
		} while ((train.getError() > 0.001));
		chronometer.stop();
		System.out.println("Training Session Completed in : " + chronometer.getMinutes() + " minutes");
		
		/* Testing */
		System.out.println("Validating Neural Network Results:");
		for (int i = 0; i < idealOutput.length; i++) {
			final double actual[] = network.computeOutputs(input[i]);
			System.out.println();
			System.out.println(Arrays.toString(input[i])
					+ ", actual=" + new DecimalFormat("##.####").format(actual[0]) + ",ideal=" + Arrays.toString(idealOutput[i]));
		}
		
		/* Error Value Plotting */
		System.out.println();
		System.out.println("Creating Training Error Values Plot");
		/* XY Chart */
		XYSeriesCollection dataset = new XYSeriesCollection();
		dataset.addSeries(series);
		
		JFreeChart chart = ChartFactory.createXYLineChart(
	            "Neural Network Training Evolution",
	            "Epochs",
	            "Error Value",
	            dataset,
	            PlotOrientation.VERTICAL,  /* Plot Orientation */
	            true,                      /* Show Legend */
	            true,                      /* Use Tooltips*/
	            false                      /* Configure chart to generate URLs? */
	            );
	        try {
	            ChartUtilities.saveChartAsJPEG(new File("TestRun/plot.png"), chart, 1250, 750); // 500 * 300 ideal size 
	        } catch (IOException e) {
	            System.err.println("Problem occurred creating chart.");
	}
	  System.out.println("Plot Done!!! [TestRun/plot.png]");
		
		
 }
	
public static void createDataSet() throws IOException{
		
		File normal = new File("DataSet/Normal");
		File[] normalFiles = normal.listFiles((FileFilter) HiddenFileFilter.VISIBLE);
		for(File file:normalFiles){
			if(file.isFile()){
				BufferedImage image = ImageIO.read(file);
				BufferedImage binary = new BufferedImage( image.getWidth(), image.getHeight(), BufferedImage.TYPE_BYTE_BINARY);
				int red, binaryPixel;
				int thresHold = 170;
				for( int i = 0; i < image.getWidth(); i++ ){
					for( int j = 0; j < image.getHeight(); j++ ){
						red = new Color(image.getRGB(i, j)).getRed();
						int alpha = new Color( image.getRGB(i, j)).getAlpha();
						if( red < thresHold ){
							binaryPixel = 0;
						} else {
							binaryPixel = 255;
						}
						binaryPixel = colorToRGB(alpha, binaryPixel, binaryPixel, binaryPixel);
						binary.setRGB(i, j, binaryPixel);
					}
				}
				ImageIO.write(binary, "png", new File("DataSet/Binary/binary_" + file.getName()));
			}
		}
		
		BufferedImage exampleImage = ImageIO.read(normalFiles[0]);
		input = new double[normalFiles.length][exampleImage.getWidth() * exampleImage.getHeight()];
		
		File binary = new File("DataSet/Binary");
		File[] binaryFiles = binary.listFiles((FileFilter) HiddenFileFilter.VISIBLE);
		int recordsCounter = 0, recordCounter = 0;
		for( File file:binaryFiles ){
			if(file.isFile()){
				BufferedImage image = ImageIO.read(file);
				for( int i = 0; i < image.getWidth(); i++ ){
					for( int j = 0; j < image.getHeight(); j++){
						int pixel = image.getRGB(i, j);
						int red = ( pixel >> 16 ) & 0xff;
						int green = ( pixel >> 8 ) & 0xff;
						int blue = ( pixel ) & 0xff;
						if( red == 255 && green == 255 && blue == 255 ){
							/* White */
							input[recordsCounter][recordCounter] = 0.0;
							recordCounter++;
						} else {
							/* Black */
							input[recordsCounter][recordCounter] = 1.0;
							recordCounter++;
						}
					}
					
				}
				recordCounter = 0;
				recordsCounter++;
			}
		}
		
	}

 
	  private static int colorToRGB(int alpha, int red, int green, int blue) {
	        int newPixel = 0;
	        newPixel += alpha;
	        newPixel = newPixel << 8;
	        newPixel += red; newPixel = newPixel << 8;
	        newPixel += green; newPixel = newPixel << 8;
	        newPixel += blue;

	        return newPixel;
	    }
	  
	}
