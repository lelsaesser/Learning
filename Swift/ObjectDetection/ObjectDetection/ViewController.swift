//
//  ViewController.swift
//  ObjectDetection
//
//  Created by lelsaesser on 25.05.19.
//  Copyright © 2019 lelsaesser. All rights reserved.
//

import UIKit
import AVKit
import Vision
import ARKit

class ViewController: UIViewController, AVCaptureVideoDataOutputSampleBufferDelegate {
    
    private var detectedLabel = "123"
    private var detectedLabelConfidence = VNConfidence()
    private var textView = UILabel(frame: CGRect(x: 20, y: 50, width: 300, height: 40))

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // start up the iPhone camera
        let captureSession = AVCaptureSession()
        captureSession.sessionPreset = .photo
        
        guard let captureDevice = AVCaptureDevice.default(for: .video) else { return }
        guard let input = try? AVCaptureDeviceInput(device: captureDevice) else { return }
        
        captureSession.addInput(input)
        captureSession.startRunning()
        
        let previewLayer = AVCaptureVideoPreviewLayer(session: captureSession)
        view.layer.addSublayer(previewLayer)
        previewLayer.frame = view.frame
        
        let dataOutput = AVCaptureVideoDataOutput()
        dataOutput.setSampleBufferDelegate(self, queue: DispatchQueue(label: "videoQueue"))
        captureSession.addOutput(dataOutput)
        
        
        // text field with outputs
        self.textView.font = UIFont.systemFont(ofSize: 15)
        self.view.addSubview(textView)
    }
    
    func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
        //print("Camera was able to capture a frame:", Date())
        
        guard let pixelBuffer: CVPixelBuffer =  CMSampleBufferGetImageBuffer(sampleBuffer) else { return }
        guard let model = try? VNCoreMLModel(for: Resnet50().model) else { return }
        
        let request = VNCoreMLRequest(model: model) { (finishedRequest, error) in
            guard let results = finishedRequest.results as? [VNClassificationObservation] else { return }
            guard let firstObservation = results.first else { return }
            
            self.detectedLabel = firstObservation.identifier
            self.detectedLabelConfidence = firstObservation.confidence
            
            print(firstObservation.identifier, firstObservation.confidence)
            self.updateTextView()
        }
        
        try? VNImageRequestHandler(cvPixelBuffer: pixelBuffer, options: [:]).perform([request])
    }
    
    func updateTextView() {
        DispatchQueue.main.async {
            let confidence = String(format: "%.2f", self.detectedLabelConfidence * 100.00)
            self.textView.text = "\(self.detectedLabel) \(confidence) %"
        }
    }
}

