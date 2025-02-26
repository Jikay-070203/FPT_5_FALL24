{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c134f98a-c7f9-48f1-80a6-5e69b305d8d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: ipykernel_launcher.py [-h] --model MODEL --data DATA [--batch BATCH]\n",
      "ipykernel_launcher.py: error: the following arguments are required: --model, --data\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.12/site-packages/IPython/core/interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import argparse\n",
    "from ultralytics import YOLO\n",
    "\n",
    "def load_yolo_model(model_name):\n",
    "    if model_name in ['yolov10', 'yolov9', 'yolov8', 'yolov7']:\n",
    "        # Load the model based on the specified version\n",
    "        model = YOLO(f\"{model_name}.pt\")  # Assumes the model files are named like 'yolov10.pt'\n",
    "        return model\n",
    "    else:\n",
    "        raise ValueError(\"Unsupported YOLO model. Please choose from ['yolov10', 'yolov9', 'yolov8', 'yolov7'].\")\n",
    "\n",
    "def main():\n",
    "    # Set up command-line argument parsing\n",
    "    parser = argparse.ArgumentParser(description=\"Load and validate YOLO models with your own data.\")\n",
    "    parser.add_argument('--model', type=str, required=True, help='Specify the YOLO model (yolov10, yolov9, yolov8, yolov7)')\n",
    "    parser.add_argument('--data', type=str, required=True, help='Specify the path to your dataset YAML file (e.g., coco.yaml)')\n",
    "    parser.add_argument('--batch', type=int, default=256, help='Batch size for validation')\n",
    "\n",
    "    args = parser.parse_args()\n",
    "\n",
    "    # Load the specified YOLO model\n",
    "    try:\n",
    "        model = load_yolo_model(args.model)\n",
    "        print(f\"Loaded {args.model} successfully.\")\n",
    "    except ValueError as e:\n",
    "        print(e)\n",
    "        return\n",
    "\n",
    "    # Validate the model with your data\n",
    "    model.val(data=args.data, batch=args.batch)\n",
    "    print(\"Validation complete.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "105030a9-00ae-4f5a-ad1a-8dbed019cee8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
