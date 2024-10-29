from ui_manager import run_app
from report_generator import generate_report
from notification_manager import show_notification

if __name__ == "__main__":
    run_app()
    
    report_file = 'estoque_relatorio'
    generate_report('database/sales.db', report_file)
    show_notification(f"Relatório gerado com sucesso: {report_file}.csv e {report_file}.pdf")
