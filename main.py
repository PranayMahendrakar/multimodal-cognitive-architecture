#!/usr/bin/env python3
"""Multimodal Cognitive Architecture Discovery - Author: Pranay M"""
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import *

console = Console()

def main():
    console.print(Panel("🧠 MULTIMODAL COGNITIVE ARCHITECTURE DISCOVERY 🧠", style="bold cyan"))
    modules = {"1": ("Architecture Discovery", ArchitectureDiscoverer()), "2": ("Modality Analysis", ModalityAnalyzer()),
               "3": ("Integration Design", IntegrationDesigner()), "4": ("Optimization", OptimizationEngine()),
               "5": ("Benchmarking", BenchmarkEvaluator()), "6": ("Transfer Learning", TransferLearner()),
               "7": ("Scalability", ScalabilityAnalyzer()), "8": ("Meta Learning", MetaLearner()),
               "9": ("Domain Adaptation", DomainAdapter()), "10": ("Synthesis", SynthesisEngine())}
    while True:
        table = Table(title="Discovery Modules")
        for k,(n,_) in modules.items(): table.add_row(k,n)
        table.add_row("0","Exit")
        console.print(table)
        c = Prompt.ask("Select", choices=list(modules.keys())+["0"])
        if c == "0": break
        query = Prompt.ask("Domain/Input")
        result = modules[c][1].discover(query)
        console.print(Panel(Markdown(result), title=modules[c][0], border_style="cyan"))

if __name__ == "__main__": main()
